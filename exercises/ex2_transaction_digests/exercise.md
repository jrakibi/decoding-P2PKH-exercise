# Exercise 2: Bitcoin Transaction Digests

In this exercise, you will learn how transaction digests are calculated for signing in SegWit transactions according to BIP143.

## Background

BIP143 introduced a new signature hash algorithm for SegWit transactions that:
- Fixes transaction malleability issues
- Enables more efficient verification
- Provides better security against signature hash optimization

The BIP143 algorithm calculates several hash components:
- **hashPrevouts**: Double SHA256 of all input outpoints
- **hashSequence**: Double SHA256 of all input sequence numbers
- **hashOutputs**: Double SHA256 of all outputs

These components are then combined with other transaction data to create the signature hash.

## Your Task

Complete the following functions in `template.py`:

1. `dsha256(data)`: Implement a double SHA256 hash function
   - Apply SHA256 twice: SHA256(SHA256(data))

2. `get_transaction_digest(inputs, outputs)`: Calculate BIP143 transaction digest components
   - Extract outpoints and sequences from inputs
   - Calculate hashPrevouts, hashSequence, and hashOutputs
   - Return these three hash components

## Testing

Your implementation will be tested against known BIP143 test vectors.

## Hints

- Remember that outpoints consist of txid (32 bytes) + vout (4 bytes)
- The sequence is the last 4 bytes of each input
- Use the provided helper functions from Exercise 1 