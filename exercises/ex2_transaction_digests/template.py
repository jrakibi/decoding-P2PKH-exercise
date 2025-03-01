import hashlib
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
    
    # Output structure
    output_bytes = (
        amount_bytes +          # value in satoshis
        script_pubkey          # includes length prefix
    )
    
    return output_bytes

def dsha256(data: bytes) -> bytes:
    """Double SHA256 hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

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