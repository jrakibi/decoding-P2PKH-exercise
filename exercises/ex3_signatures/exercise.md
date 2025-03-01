# Exercise 3: Bitcoin Transaction Signatures

In this exercise, you will implement a function to sign transaction digests according to Bitcoin's requirements.

## Background

Bitcoin uses ECDSA signatures with the secp256k1 curve. These signatures must follow specific rules:
- They must be deterministic (RFC 6979)
- They must use low-S values (BIP62)
- They must be encoded in DER format
- They must include a SIGHASH byte (usually SIGHASH_ALL = 0x01)

The low-S requirement is particularly important as it prevents transaction malleability. If S > N/2 (where N is the curve order), it must be replaced with N-S.

## Your Task

Complete the following function in `template.py`:

1. `sign(private_key, commitment)`: Sign a transaction digest with a private key
   - Create a deterministic signature (RFC 6979)
   - Ensure the signature uses low-S values (BIP62)
   - Encode the signature in DER format
   - Append the SIGHASH_ALL byte (0x01)

## Testing

Your implementation will be tested against known BIP143 test vectors.

## Hints

- Use the `ecdsa` library's `SigningKey` class for creating signatures
- Check if S > N/2 and replace it with N-S if necessary
- The SECP256k1 curve order (N) is provided by `SECP256k1.order`
- DER encoding can be done with `util.sigencode_der` 