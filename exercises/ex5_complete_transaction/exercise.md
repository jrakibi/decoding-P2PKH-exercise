# Exercise 5: Complete Bitcoin Transaction

In this exercise, you will implement a function to assemble a complete SegWit transaction, bringing together all the components from the previous exercises.

## Background

A complete SegWit transaction includes:
- Version (4 bytes)
- Marker (1 byte, value 0x00)
- Flag (1 byte, value 0x01)
- Input count (varint)
- Inputs (variable length)
- Output count (varint)
- Outputs (variable length)
- Witness data (variable length)
- Locktime (4 bytes)

The witness data is included after all inputs and outputs, unlike in legacy transactions where signatures are part of the scriptSig.

## Your Task

Complete the following function in `template.py`:

1. `assemble_transaction(version, inputs, outputs, witnesses, locktime)`: Assemble a complete SegWit transaction
   - Include version, marker, flag, inputs, outputs, witness data, and locktime
   - Format the transaction according to BIP144 (SegWit transaction format)
   - Ensure all components are properly serialized

## Testing

Your implementation will be tested against known BIP143 test vectors.

## Hints

- The marker and flag bytes (0x00 and 0x01) indicate this is a SegWit transaction
- Each input's witness data must be in the same order as the inputs
- Empty witness data for an input is represented as 0x00
- The locktime is a 4-byte little-endian value 