"""
Exercise 4: Witness Data
This exercise focuses on creating witness data for SegWit transactions.
"""

def get_pub_from_priv(private_key: bytes) -> bytes:
    """
    Derive a compressed public key from a private key.
    
    TODO: Implement public key derivation:
    1. Derive the public key point from the private key using secp256k1
    2. Convert to compressed format (33 bytes: 0x02/0x03 + x-coordinate)
    
    Parameters:
        private_key (bytes): The private key
    
    Returns:
        bytes: The compressed public key
    """
    # Your code here
    pass

def sign(private_key: bytes, digest: bytes) -> bytes:
    """
    Sign a transaction digest with a private key.
    
    TODO: This should be the same implementation as in Exercise 3.
    
    Parameters:
        private_key (bytes): The private key to sign with
        digest (bytes): The transaction digest to sign
    
    Returns:
        bytes: The DER-encoded signature with SIGHASH_ALL appended
    """
    # Your code here
    pass

def get_p2wpkh_witness(private_key: bytes, digest: bytes) -> bytes:
    """
    Create a P2WPKH witness stack.
    
    TODO: Implement witness stack creation:
    1. Create a signature using the private key and digest
    2. Get the public key from the private key
    3. Create witness stack: [signature, pubkey]
    4. Return the serialized witness stack
    
    Parameters:
        private_key (bytes): The private key to sign with
        digest (bytes): The transaction digest to sign
    
    Returns:
        bytes: The serialized witness stack
    """
    # Your code here
    pass 