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

def assemble_transaction(
    version: int,
    inputs: List[bytes],
    outputs: List[bytes],
    witnesses: List[bytes],
    locktime: int
) -> bytes:
    """
    Assemble a complete SegWit transaction.
    
    Args:
        version: Transaction version (usually 1 or 2)
        inputs: List of serialized inputs
        outputs: List of serialized outputs
        witnesses: List of witness data (one per input)
        locktime: Transaction locktime
        
    Returns:
        Complete serialized SegWit transaction
    """
    # 4-byte version in little-endian
    tx_version = int_to_little_endian(version, 4)
    
    # Marker and flag for SegWit
    marker_flag = b'\x00\x01'
    
    # Number of inputs (varint)
    in_count = varint(len(inputs))
    
    # Serialize inputs
    serialized_inputs = b''.join(inputs)
    
    # Number of outputs (varint)
    out_count = varint(len(outputs))
    
    # Serialize outputs
    serialized_outputs = b''.join(outputs)
    
    # Serialize witness data
    serialized_witnesses = b''.join(witnesses)
    
    # Locktime (4 bytes)
    tx_locktime = int_to_little_endian(locktime, 4)
    
    # Combine all components
    return (
        tx_version +
        marker_flag +
        in_count +
        serialized_inputs +
        out_count +
        serialized_outputs +
        serialized_witnesses +
        tx_locktime
    ) 