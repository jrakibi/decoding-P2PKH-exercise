# Bitcoin Transaction Programming Exercises

This repository contains a series of progressive exercises to learn about Bitcoin transaction creation and signing, with a focus on SegWit transactions following the BIP143 standard.

## Getting Started

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Complete the implementation in each exercise's template.py file

## Exercise Structure

The exercises are designed to build on each other, gradually introducing more complex concepts:

### Exercise 1: Transaction Basics
Learn about the basic structure of Bitcoin transactions and implement functions to create transaction inputs and outputs.

### Exercise 2: Transaction Digests
Learn how transaction digests are calculated for signing in SegWit transactions according to BIP143.

### Exercise 3: Signatures
Implement a function to sign transaction digests according to Bitcoin's requirements, including deterministic signatures and low-S values.

### Exercise 4: Witness Data
Create witness data for P2WPKH (Pay-to-Witness-Public-Key-Hash) inputs.

### Exercise 5: Complete Transaction
Assemble a complete SegWit transaction, bringing together all the components from the previous exercises.

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