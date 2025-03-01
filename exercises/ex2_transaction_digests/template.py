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

# TODO: Implement this function
def dsha256(data: bytes) -> bytes:
    """
    Double SHA256 hash.
    
    Args:
        data: Data to hash
        
    Returns:
        Double SHA256 hash: SHA256(SHA256(data))
    """
    # Your implementation here
    pass

# TODO: Implement this function
def get_transaction_digest(
    inputs: List[bytes],
    outputs: List[bytes]
) -> tuple[bytes, bytes, bytes]:
    """
    Calculate BIP143 transaction digest components.
    
    Args:
        inputs: List of serialized inputs
        outputs: List of serialized outputs
        
    Returns:
        Tuple of (hashPrevouts, hashSequence, hashOutputs)
    """
    # Your implementation here
    pass 