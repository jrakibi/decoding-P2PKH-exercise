# Exercise 3: Signatures

In this exercise, you'll implement ECDSA signature generation for Bitcoin transactions.

## Your Task

Complete the function in `template.py`:

1. `sign`: Create an ECDSA signature
   - Generate a deterministic nonce (k) using RFC6979
   - Create the signature using the secp256k1 curve
   - Apply Low-S value normalization (if S > N/2, use N-S instead)
   - Format the signature in DER encoding
   - Append the SIGHASH_ALL byte (0x01)

## Testing

Run the tests:
```bash
python -m pytest test_exercise3.py -v
```

## Hints
- Use the `ecdsa` and `cryptography` libraries
- For deterministic k, read [RFC6979](https://tools.ietf.org/html/rfc6979)
- DER encoding format: 0x30 [length] 0x02 [r-length] [r] 0x02 [s-length] [s]
- The secp256k1 curve has an order (N) of 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 