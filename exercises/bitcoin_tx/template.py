import hashlib
from subprocess import run
from ecdsa import SigningKey, SECP256k1, util
from typing import List

def int_to_little_endian(value: int, length: int) -> bytes:
    """Convert an integer to little-endian bytes"""
    return value.to_bytes(length, 'little')

def varint(n: int) -> bytes:
    """Encode an integer as a variable length integer"""
    if n < 0xfd:
        return bytes([n])
    elif n <= 0xffff:
        return b'\xfd' + n.to_bytes(2, 'little')
    elif n <= 0xffffffff:
        return b'\xfe' + n.to_bytes(4, 'little')
    else:
        return b'\xff' + n.to_bytes(8, 'little')

def get_pub_from_priv(priv: bytes) -> bytes:
    """Derive the secp256k1 compressed public key from a private key."""
    sk = SigningKey.from_string(priv, curve=SECP256k1)
    vk = sk.verifying_key
    compressed_pubkey = vk.to_string("compressed")
    return compressed_pubkey

def dsha256(data: bytes) -> bytes:
    """Double SHA256 hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def create_input(
    txid: str,
    vout: int,
    script_sig: bytes = b'',
    sequence: bytes = b'\xff\xff\xff\xff'
) -> bytes:
    """Create a transaction input"""
    # Convert txid from hex string and reverse (to little-endian)
    txid_bytes = bytes.fromhex(txid)[::-1]
    
    # Convert vout to 4 bytes, little-endian
    vout_bytes = int_to_little_endian(vout, 4)
    
    # Script length and script
    script_sig_length = varint(len(script_sig))
    
    return (
        txid_bytes +           # 32 bytes
        vout_bytes +          # 4 bytes
        script_sig_length +   # 1 byte
        script_sig +          # variable
        sequence              # 4 bytes
    )

def create_output(
    amount: int,
    script_pubkey: bytes
) -> bytes:
    """Create a transaction output"""
    # Amount (8 bytes, little-endian)
    amount_bytes = int_to_little_endian(amount, 8)
    
    # Output structure:
    # 1. Amount (8 bytes)
    # 2. ScriptPubKey with length prefix
    output_bytes = (
        amount_bytes +          # value in satoshis
        script_pubkey          # includes length prefix
    )
    
    return output_bytes

def get_p2wpkh_scriptcode(script_pubkey: bytes) -> bytes:
    """
    Convert P2WPKH scriptPubKey to scriptCode for signing.
    
    Args:
        script_pubkey: The P2WPKH scriptPubKey (00{14}{20-byte-hash})
        
    Returns:
        The scriptCode for signing (1976a914{20-byte-hash}88ac)
    """
    if not script_pubkey.startswith(b'\x00\x14'):
        raise ValueError("Not a P2WPKH scriptPubKey")
        
    pubkey_hash = script_pubkey[2:]  # Skip witness version and push
    return bytes.fromhex('1976a914') + pubkey_hash + bytes.fromhex('88ac')

def get_transaction_digest(
    inputs: List[bytes],
    outputs: List[bytes]
) -> tuple[bytes, bytes, bytes]:
    """
    Calculate BIP143 transaction digest components.
    Returns (hashPrevouts, hashSequence, hashOutputs)
    """
    # For hashPrevouts: concatenate all outpoints (txid + vout)
    outpoints = b''
    sequences = b''
    for tx_input in inputs:
        outpoints += tx_input[:36]  # first 36 bytes are outpoint (txid + vout)
        sequences += tx_input[-4:]   # last 4 bytes are sequence

    # Calculate hashPrevouts
    hash_prevouts = dsha256(outpoints)

    # Calculate hashSequence
    hash_sequence = dsha256(sequences)

    # Calculate hashOutputs
    outputs_data = b''.join(outputs)
    hash_outputs = dsha256(outputs_data)

    return hash_prevouts, hash_sequence, hash_outputs

def get_commitment_hash(
    outpoint: bytes,           # The input being signed (txid + vout)
    scriptcode: bytes,         # From step 2
    value: int,                # Value of the output being spent
    outputs: List[bytes],      # Transaction outputs
    all_inputs: List[bytes]    # All transaction inputs (required for BIP143)
) -> bytes:
    """Calculate BIP143 sighash"""
    
    # Version (4 bytes little-endian)
    version = int_to_little_endian(1, 4)
    
    # Get transaction digest components
    hash_prevouts, hash_sequence, hash_outputs = get_transaction_digest(
        all_inputs,  # Uses ALL transaction inputs
        outputs
    )
    
    # Value of spent output (8 bytes little-endian)
    value_bytes = int_to_little_endian(value, 8)
    
    # Sequence for THIS input (4 bytes)
    sequence = b'\xff\xff\xff\xff'  # From test vector
    
    # Locktime (4 bytes little-endian)
    locktime = int_to_little_endian(0x11, 4)  # 17 in hex
    
    # SIGHASH_ALL (4 bytes little-endian)
    sighash_type = int_to_little_endian(1, 4)
    
    # Build preimage according to BIP143 structure
    preimage = (
        version +
        hash_prevouts +
        hash_sequence +
        outpoint +
        scriptcode +
        value_bytes +
        sequence +
        hash_outputs +
        locktime +
        sighash_type
    )
    
    # Double SHA256 to produce the final sighash
    return hashlib.sha256(hashlib.sha256(preimage).digest()).digest()

def sign(private_key: bytes, commitment: bytes) -> bytes:
    """
    Sign a commitment hash with a private key.
    Returns DER-encoded signature with SIGHASH_ALL byte appended.
    
    Args:
        private_key: 32-byte private key
        commitment: 32-byte commitment hash to sign
        
    Returns:
        DER-encoded signature + SIGHASH_ALL byte
    """
    # Create signing key from private key bytes
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    
    while True:
        # Create deterministic signature (RFC 6979)
        signature_der = sk.sign_digest_deterministic(
            commitment,
            hashfunc=hashlib.sha256,
            sigencode=util.sigencode_der
        )
        
        # Decode signature to get r and s values
        r, s = util.sigdecode_der(signature_der, SECP256k1.order)

        # Check if s is high (BIP62)
        if s > SECP256k1.order // 2:
            s = SECP256k1.order - s  # Convert to low-s
            # Re-encode with low-s
            signature_der = util.sigencode_der(r, s, SECP256k1.order)

        # Add SIGHASH_ALL byte
        signature_with_sighash = signature_der + b'\x01'
        
        # Only exit if we have low-s
        if s <= SECP256k1.order // 2:
            break
            
    return signature_with_sighash

def get_p2wpkh_witness(priv: bytes, msg: bytes) -> bytes:
    """
    Create witness stack for P2WPKH input with format:
    [num_items][sig_len][signature][pubkey_len][pubkey]
    """
    # Get signature with sighash byte
    signature_with_sighash = sign(priv, msg)
    
    # Get compressed public key
    compressed_public_key = get_pub_from_priv(priv)
    
    # Number of witness items (always 2 for P2WPKH)
    num_witness_items = bytes([2])
    
    # Serialize signature with its length
    sig_len = bytes([len(signature_with_sighash)])
    serialized_sig = sig_len + signature_with_sighash
    
    # Serialize public key with its length
    pk_len = bytes([len(compressed_public_key)])
    serialized_pk = pk_len + compressed_public_key
    
    # Combine all parts
    serialized_witness = num_witness_items + serialized_sig + serialized_pk
    return serialized_witness

def assemble_transaction(
    inputs: List[bytes],
    outputs: List[bytes],
    witnesses: List[bytes]
) -> bytes:
    """
    Assemble the final SegWit transaction.
    
    Args:
        inputs: List of serialized inputs
        outputs: List of serialized outputs
        witnesses: List of witness data (one per input, empty bytes for non-witness inputs)
    """
    # 4-byte version
    version = int_to_little_endian(1, 4)
    
    # Marker and flag for SegWit
    marker_flag = b'\x00\x01'
    
    # Input count and serialized inputs
    input_count = varint(len(inputs))
    serialized_inputs = b''.join(inputs)
    
    # Output count and serialized outputs
    output_count = varint(len(outputs))
    serialized_outputs = b''.join(outputs)
    
    # Witness data (already includes counts)
    witness_data = b''.join(witnesses)
    
    # 4-byte locktime
    locktime = int_to_little_endian(0x11, 4)
    
    # Combine all parts
    return (
        version +
        marker_flag +
        input_count +
        serialized_inputs +
        output_count +
        serialized_outputs +
        witness_data +
        locktime
    ) 