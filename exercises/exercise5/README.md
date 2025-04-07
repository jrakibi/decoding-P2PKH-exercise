# Exercise 5: Complete Transaction

In this exercise, you'll implement functions to assemble a complete SegWit transaction.

## Your Task

Complete the functions in `template.py`:

1. `int_to_little_endian`: Convert an integer to little-endian bytes
   - Convert the integer to bytes of specified length
   - Ensure the byte order is little-endian

2. `varint`: Implement variable-length integer encoding
   - < 0xfd: encode as a single byte
   - ≤ 0xffff: encode as 0xfd + 2 bytes little-endian
   - ≤ 0xffffffff: encode as 0xfe + 4 bytes little-endian
   - > 0xffffffff: encode as 0xff + 8 bytes little-endian

3. `assemble_transaction`: Assemble a complete SegWit transaction
   - Add version number (4 bytes)
   - Add SegWit marker (0x00) and flag (0x01)
   - Add inputs and outputs with proper counts
   - Add witness data for each input
   - Add locktime

## Testing

Run the tests:
```bash
python -m pytest test_exercise5.py -v
```

## Hints
- The final transaction is a concatenation of all fields in the correct order
- Pay special attention to the witness data structure; each input must have its own witness stack
- Complete SegWit transaction structure: version + marker + flag + tx_in_count + tx_ins + tx_out_count + tx_outs + witness + locktime 