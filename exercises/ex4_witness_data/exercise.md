# Exercise 4: Bitcoin Witness Data

In this exercise, you will implement a function to create witness data for P2WPKH (Pay-to-Witness-Public-Key-Hash) inputs.

## Background

SegWit (Segregated Witness) transactions separate signature data from transaction data. For P2WPKH inputs, the witness data consists of:
- A signature that satisfies the spending conditions
- The public key that corresponds to the key hash in the scriptPubKey

The witness stack for a P2WPKH input has the following format:
- Number of witness items (2 for P2WPKH)
- Signature length + signature (with SIGHASH byte)
- Public key length + public key

## Your Task

Complete the following function in `template.py`:

1. `get_pub_from_priv(priv)`: Derive a compressed public key from a private key
   - Use the secp256k1 curve
   - Return the compressed public key format

2. `get_p2wpkh_witness(priv, msg)`: Create a witness stack for a P2WPKH input
   - Sign the message with the private key
   - Get the compressed public key
   - Format the witness data correctly

## Testing

Your implementation will be tested against known BIP143 test vectors.

## Hints

- The witness format is: [num_items][sig_len][signature][pubkey_len][pubkey]
- For P2WPKH, there are always 2 witness items
- Use the `sign` function from Exercise 3 to create the signature
- Remember to include length prefixes for each item 