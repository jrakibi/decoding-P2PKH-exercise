# Exercise 4: Witness Data

In this exercise, you'll implement witness data creation for SegWit transactions.

## Your Task

Complete the functions in `template.py`:

1. `get_pub_from_priv`: Derive a public key from a private key
   - Derive the public key point using secp256k1
   - Format as compressed (33 bytes: 0x02/0x03 + x-coordinate)

2. `sign`: Create a signature (same as Exercise 3)
   - Reuse your signature implementation from Exercise 3

3. `get_p2wpkh_witness`: Create a P2WPKH witness stack
   - Create a signature using the private key and digest
   - Get the public key from the private key
   - Format as witness stack with signature and pubkey
   - Properly serialize the witness stack

## Testing

Run the tests:
```bash
python -m pytest test_exercise4.py -v
```

## Hints
- SegWit witness stack format: [number of items, item1 length, item1, item2 length, item2, ...]
- P2WPKH witness stack has exactly 2 items: signature and public key
- Use the `ecdsa` library for key operations
- The public key must be in compressed format 