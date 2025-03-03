# Bitcoin Transaction Programming Exercises

This repository contains a series of progressive exercises to learn about Bitcoin transaction creation and signing, with a focus on SegWit transactions following the BIP143 standard.

## Getting Started

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```


2. Work through each exercise sequentially, completing the implementation in each `template.py` file

## Exercise Progression

### Exercise 1: Transaction Basics
**What you'll learn:** The fundamental structure of Bitcoin transactions
- Create transaction inputs (references to previous transaction outputs)
- Create transaction outputs (new spendable amounts with locking scripts)
- Understand transaction version, locktime, and sequence numbers
- Practice serializing transaction components to binary format

### Exercise 2: Transaction Digests
**What you'll learn:** How transaction data is prepared for signing in SegWit
- Implement BIP143 digest algorithm for SegWit transactions
- Understand how the digest algorithm prevents transaction malleability
- Learn to handle different input types (P2WPKH, P2WSH)
- Practice double-SHA256 hashing and byte manipulation

### Exercise 3: Signatures
**What you'll learn:** Bitcoin's signature requirements and standards
- Create ECDSA signatures using the secp256k1 curve
- Implement deterministic signatures (RFC6979)
- Apply Low-S value normalization for BIP62 compliance
- Format signatures in DER encoding as required by Bitcoin

### Exercise 4: Witness Data
**What you'll learn:** SegWit's witness structure
- Create witness stacks for P2WPKH inputs
- Understand the witness serialization format
- Learn how signatures and public keys are organized in witness data
- See how witness data is separated from the transaction body

### Exercise 5: Complete Transaction
**What you'll learn:** Putting it all together
- Assemble a complete SegWit transaction from all components
- Calculate transaction fees
- Verify the final transaction structure
- Create transactions that can be broadcast to the Bitcoin network

## Testing Your Implementation

Each exercise includes comprehensive tests to verify your code against known test vectors:


## Testing Your Implementation

Each exercise includes a test file that verifies your implementation against known test vectors from BIP143. To run the tests for an exercise:

```bash
cd exercises/ex1_transaction_basics
pytest test_solution.py -v
```

## Important Concepts

- **Little-Endian vs Big-Endian**: Bitcoin uses little-endian byte order for most values
- **DER Encoding**: Bitcoin signatures must follow strict DER encoding rules
- **Low-S Values**: For BIP62 compliance, if s > n/2, use n-s instead (where n is the curve order)
- **SegWit**: Segregated Witness separates signature data from transaction data to improve scalability
- **BIP143**: Introduced a new signature verification scheme for SegWit transactions that fixes transaction malleability issues

## Resources

- [Bitcoin Developer Reference](https://developer.bitcoin.org/reference/)
- [BIP143 Specification](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)
- [Bitcoin Transaction Structure](https://en.bitcoin.it/wiki/Transaction)
- [SegWit Benefits](https://bitcoincore.org/en/2016/01/26/segwit-benefits/)