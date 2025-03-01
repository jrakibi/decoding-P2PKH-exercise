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

# TODO: Implement this function
def create_input(
    txid: str,
    vout: int,
    script_sig: bytes = b'',
    sequence: bytes = b'\xff\xff\xff\xff'
) -> bytes:
    """
    Create a transaction input.
    
    Args:
        txid: Transaction ID as a hex string
        vout: Output index to spend
        script_sig: Script that satisfies spending conditions
        sequence: Sequence number (default: 0xffffffff)
        
    Returns:
        Serialized transaction input
    """
    # Your implementation here
    pass

# TODO: Implement this function
def create_output(
    amount: int,
    script_pubkey: bytes
) -> bytes:
    """
    Create a transaction output.
    
    Args:
        amount: Value in satoshis
        script_pubkey: Script that sets spending conditions
        
    Returns:
        Serialized transaction output
    """
    # Your implementation here
    pass

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