# Bitcoin Transaction Signing Exercise

This exercise focuses on implementing key components of Bitcoin transaction creation and signing, with emphasis on SegWit transactions following the BIP143 standard.

## Background

Bitcoin transactions consist of inputs (previous transaction outputs being spent) and outputs (new UTXOs being created). Segwit (Segregated Witness) transactions separate signature data from transaction data to improve scalability.

BIP143 introduced a new signature verification scheme for SegWit transactions that fixes transaction malleability issues and enables more efficient verification.

## Getting Started

1. Install the required dependency:

```bash
pip install ecdsa
```

2. Complete the implementation in `exercises/bitcoin_tx/template.py`

## Tasks

Implement the following functions:

1. `sign(private_key, commitment)`: Sign a transaction digest with a private key following Bitcoin's signature requirements
   - Create a deterministic signature (RFC 6979)
   - Ensure the signature uses low-S values (BIP62)
   - Append the SIGHASH_ALL byte

2. `get_p2wpkh_witness(priv, msg)`: Create a proper witness stack for a P2WPKH input
   - Format: [num_items][sig_len][signature][pubkey_len][pubkey]

3. `assemble_transaction(inputs, outputs, witnesses)`: Assemble the final SegWit transaction
   - Include version, marker, flag, inputs, outputs, witness data, and locktime

## Testing

Your implementation will be tested against known test vectors from BIP143 to ensure compatibility with the Bitcoin protocol.

## Important Notes

- Pay attention to byte ordering (little-endian vs big-endian)
- The signature must follow strict DER encoding rules
- For BIP62 compliance, if s > n/2, use n-s instead (where n is the curve order)