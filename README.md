# Bitcoin Transaction Exercise

In this exercise, you will implement various components of Bitcoin transaction creation and signing, following the BIP143 specification for SegWit transactions.

## Setup

1. Fork this repository
2. Clone your fork
3. Implement the required functions in `solution.py`
4. Push your changes to trigger the tests

## Tasks

### 1. Basic Transaction Structure
Implement the following functions in `solution.py`:

- `create_basic_tx(version, inputs, outputs, locktime, segwit=False)`
- `create_input(txid, vout, script_sig, sequence)`
- `create_output(amount, script_pubkey)`

### 2. P2WPKH Script Handling
Implement:
- `get_p2wpkh_scriptcode(script_pubkey)`

### 3. Transaction Digest Components
Implement:
- `get_transaction_digest(inputs, outputs)`

### 4. BIP143 Commitment Hash
Implement:
- `get_commitment_hash(outpoint, scriptcode, value, outputs, all_inputs)`

### 5. Transaction Signing
Implement:
- `sign(private_key, commitment)`
- `get_p2wpkh_witness(priv, msg)`

### 6. Final Transaction Assembly
Implement:
- `assemble_transaction(inputs, outputs, witnesses)`

## Testing

Your implementation will be tested against known test vectors from BIP143. The GitHub workflow will run automatically when you push your changes.

## Requirements

- All functions must handle bytes and integers as specified in the function signatures
- Follow BIP143 specification for SegWit transaction signing
- Ensure proper handling of little-endian encoding where required