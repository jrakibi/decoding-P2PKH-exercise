"""
Exercise 1: Transaction Basics
This exercise focuses on creating and serializing basic Bitcoin transaction components.
"""

def create_input(txid: str, vout: int, script_sig: bytes = b'', sequence: bytes = b'\xff\xff\xff\xff') -> bytes:
    """
    Create a transaction input.
    
    TODO: Implement this function to create a serialized transaction input:
    1. Convert txid from hex string to bytes and reverse it (little-endian)
    2. Convert vout to 4 bytes in little-endian
    3. Add varint for script_sig length
    4. Add script_sig
    5. Add sequence
    
    Parameters:
        txid (str): The transaction ID (hex string)
        vout (int): The output index
        script_sig (bytes): The unlocking script (default empty)
        sequence (bytes): The sequence number (default 0xffffffff)
    
    Returns:
        bytes: The serialized transaction input
    """
    # Your code here
    pass

def create_output(amount: int, script_pubkey: bytes) -> bytes:
    """
    Create a transaction output.
    
    TODO: Implement this function to create a serialized transaction output:
    1. Convert amount to 8 bytes in little-endian
    2. Add script_pubkey with its length
    
    Parameters:
        amount (int): The output amount in satoshis
        script_pubkey (bytes): The locking script
    
    Returns:
        bytes: The serialized transaction output
    """
    # Your code here
    pass

def create_basic_tx(version: int, inputs: list, outputs: list, locktime: int, segwit: bool = True) -> bytes:
    """
    Create a basic Bitcoin transaction.
    
    TODO: Implement this function to create a serialized transaction:
    1. Add version as 4 bytes in little-endian
    2. If segwit, add marker (0x00) and flag (0x01)
    3. Add number of inputs (varint)
    4. Add all inputs
    5. Add number of outputs (varint)
    6. Add all outputs
    7. Add locktime as 4 bytes in little-endian
    
    Parameters:
        version (int): Transaction version
        inputs (list): List of serialized inputs
        outputs (list): List of serialized outputs
        locktime (int): Transaction locktime
        segwit (bool): Whether to create a SegWit transaction
    
    Returns:
        bytes: The serialized transaction
    """
    # Your code here
    pass 