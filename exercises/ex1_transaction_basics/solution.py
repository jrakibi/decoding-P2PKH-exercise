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
    
    # Script length
    script_pubkey_length = varint(len(script_pubkey))
    
    # Output structure:
    # 1. Amount (8 bytes)
    # 2. Script length (varint)
    # 3. ScriptPubKey
    output_bytes = (
        amount_bytes +          # value in satoshis
        script_pubkey_length +  # script length
        script_pubkey           # actual script
    )
    
    return output_bytes

def create_basic_tx(
    version: int,
    inputs: list,
    outputs: list,
    locktime: int,
    segwit: bool = False
) -> bytes:
    """
    Create a basic transaction from inputs and outputs.
    
    Args:
        version: Transaction version
        inputs: List of serialized inputs
        outputs: List of serialized outputs
        locktime: Transaction locktime
        segwit: Whether to include segwit marker and flag
        
    Returns:
        Serialized transaction
    """
    # 4-byte version in little-endian
    tx_version = int_to_little_endian(version, 4)
    
    # Marker + Flag for segwit (only if segwit=True)
    marker_flag = b'\x00\x01' if segwit else b''
    
    # Number of inputs (varint)
    in_count = varint(len(inputs))
    
    # Number of outputs (varint)
    out_count = varint(len(outputs))
    
    # Serialize inputs
    serialized_inputs = b''.join(inputs)
    
    # Serialize outputs
    serialized_outputs = b''.join(outputs)
    
    # Locktime (4 bytes)
    tx_locktime = int_to_little_endian(locktime, 4)
    
    # Combine them
    return (
        tx_version +
        marker_flag +
        in_count +
        serialized_inputs +
        out_count +
        serialized_outputs +
        tx_locktime
    ) 