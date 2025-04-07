# Exercise 2: Transaction Digests

In this exercise, you'll implement the BIP143 digest algorithm for SegWit transactions.

## Your Task

Complete the functions in `template.py`:

1. `dsha256`: Implement double SHA256 hashing
   - First SHA256 hash
   - Second SHA256 hash on the result

2. `get_transaction_digest`: Implement BIP143 digest algorithm
   - Hash all previous outputs
   - Hash all sequence numbers
   - Add current input details
   - Add script code and amount
   - Hash all outputs
   - Add locktime and sighash type

## Testing

Run the tests:
```bash
python -m pytest test_exercise2.py -v
```

## Hints
- Read the [BIP143 specification](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)
- Use the `hashlib.sha256()` function for SHA256 hashing
- All inputs are provided as bytes, no need for conversion
- The order of fields in the digest is important 