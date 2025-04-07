# Exercise 1: Transaction Basics

In this exercise, you'll implement the basic building blocks of Bitcoin transactions:
- Transaction inputs
- Transaction outputs
- Basic transaction structure

## Your Task

Complete the functions in `template.py`:

1. `create_input`: Create a serialized transaction input
   - Convert transaction ID to little-endian bytes
   - Add output index (vout)
   - Add script signature
   - Add sequence number

2. `create_output`: Create a serialized transaction output
   - Convert amount to little-endian bytes
   - Add script public key

3. `create_basic_tx`: Assemble a complete transaction
   - Add version
   - Add inputs and outputs
   - Add SegWit marker and flag if needed
   - Add locktime

## Testing

Run the tests:
```bash
python -m pytest test_exercise1.py -v
```

## Hints
- Use `bytes.fromhex()` to convert hex strings to bytes
- Remember Bitcoin uses little-endian for most values
- The varint format is used for variable length fields 