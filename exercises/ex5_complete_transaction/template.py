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
    # Your implementation here
    pass 