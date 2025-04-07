"""
Exercise 3: Signatures
This exercise focuses on creating ECDSA signatures for Bitcoin transactions.
"""

def sign(private_key: bytes, digest: bytes) -> bytes:
    """
    Sign a transaction digest with a private key.
    
    TODO: Implement ECDSA signature generation:
    1. Generate a deterministic k value (RFC6979)
    2. Create an ECDSA signature using the secp256k1 curve
    3. Apply Low-S value normalization (BIP62)
    4. Format the signature in DER encoding
    5. Add the SIGHASH_ALL byte (0x01) at the end
    
    Parameters:
        private_key (bytes): The private key to sign with
        digest (bytes): The transaction digest to sign
    
    Returns:
        bytes: The DER-encoded signature with SIGHASH_ALL appended
    """
    # Your code here
    pass 