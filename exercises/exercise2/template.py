"""
Exercise 2: Transaction Digests
This exercise focuses on implementing the BIP143 digest algorithm for SegWit transactions.
"""

# These functions from Exercise 1 are provided for you
def create_input(txid: str, vout: int, script_sig: bytes = b'', sequence: bytes = b'\xff\xff\xff\xff') -> bytes:
    """Create a transaction input (provided from Exercise 1)."""
    # Convert txid from hex string to bytes and reverse it (little-endian)
    txid_bytes = bytes.fromhex(txid)[::-1]
    
    # Convert vout to 4 bytes in little-endian
    vout_bytes = vout.to_bytes(4, 'little')
    
    # Add script length as varint
    script_len = len(script_sig).to_bytes(1, 'little')
    
    # Return serialized input
    return txid_bytes + vout_bytes + script_len + script_sig + sequence

def create_output(amount: int, script_pubkey: bytes) -> bytes:
    """Create a transaction output (provided from Exercise 1)."""
    # Convert amount to 8 bytes in little-endian
    amount_bytes = amount.to_bytes(8, 'little')
    
    # Return serialized output (no need for script length as it's included in script_pubkey)
    return amount_bytes + script_pubkey

def dsha256(data: bytes) -> bytes:
    """
    Perform double SHA256 hashing.
    
    TODO: Implement double SHA256:
    1. Hash the data with SHA256
    2. Hash the result again with SHA256
    
    Parameters:
        data (bytes): Data to hash
    
    Returns:
        bytes: The double SHA256 hash
    """
    # Your code here
    pass

def get_transaction_digest(version: bytes, 
                         prev_outs: bytes,
                         sequences: bytes, 
                         output_to_spend: bytes,
                         script_code: bytes,
                         amount: bytes,
                         sequence: bytes,
                         outputs: bytes,
                         locktime: bytes,
                         sighash: bytes) -> bytes:
    """
    Create the transaction digest according to BIP143 specification.
    
    TODO: Implement BIP143 digest algorithm:
    1. Hash prevouts (dsha256 of all input outpoints)
    2. Hash sequence numbers (dsha256 of all input sequences)
    3. Copy the outpoint of this input
    4. Add the script code
    5. Add the amount
    6. Add the sequence
    7. Hash outputs (dsha256 of all outputs)
    8. Add locktime
    9. Add sighash type
    
    Parameters:
        version (bytes): Transaction version
        prev_outs (bytes): Serialized previous outputs
        sequences (bytes): Serialized sequence numbers
        output_to_spend (bytes): The outpoint being spent
        script_code (bytes): The script code for signing
        amount (bytes): The amount being spent
        sequence (bytes): The sequence number
        outputs (bytes): Serialized outputs
        locktime (bytes): Transaction locktime
        sighash (bytes): Signature hash type
    
    Returns:
        bytes: The transaction digest to be signed
    """
    # Your code here
    pass 