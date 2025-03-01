import hashlib
from ecdsa import SigningKey, SECP256k1, util

def int_to_little_endian(value: int, length: int) -> bytes:
    """Convert an integer to little-endian bytes"""
    return value.to_bytes(length, 'little')

def dsha256(data: bytes) -> bytes:
    """Double SHA256 hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

# TODO: Implement this function
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
    # Your implementation here
    pass 