# Exercise 1: Bitcoin Transaction Basics

In this exercise, you will learn about the basic structure of Bitcoin transactions and implement functions to create transaction inputs and outputs.

## Background

Bitcoin transactions consist of:
- **Version**: 4-byte integer indicating the transaction format version
- **Inputs**: Previous transaction outputs being spent
- **Outputs**: New UTXOs (Unspent Transaction Outputs) being created
- **Locktime**: When the transaction can be added to the blockchain

Each input contains:
- **Outpoint**: Reference to the output being spent (txid + vout)
- **ScriptSig**: Script that satisfies the conditions of the output being spent
- **Sequence**: Used for timelocks and RBF (Replace-By-Fee)

Each output contains:
- **Value**: Amount in satoshis
- **ScriptPubKey**: Script that sets the conditions for spending this output

## Your Task

Complete the following functions in `template.py`:

1. `create_input(txid, vout, script_sig, sequence)`: Create a transaction input
   - Convert txid to little-endian bytes
   - Format vout as 4-byte little-endian
   - Include script_sig with its length prefix
   - Add sequence number

2. `create_output(amount, script_pubkey)`: Create a transaction output
   - Format amount as 8-byte little-endian
   - Include script_pubkey with its length prefix

## Testing

Your implementation will be tested against known Bitcoin transaction formats.

## Hints

- Pay close attention to byte ordering (little-endian vs big-endian)
- Use the provided helper functions for converting integers to little-endian bytes
- Remember to include length prefixes for variable-length fields 