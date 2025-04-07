# P2PKH Transaction Decoding Exercise

Learn Bitcoin transaction creation and signing by implementing P2PKH transaction decoding.

## Setup
```bash
pip install -r requirements.txt
```

## Exercises

The repository contains 5 progressive exercises:

1. **Transaction Basics**: Create and serialize transaction inputs and outputs
2. **Transaction Digests**: Implement the BIP143 digest algorithm
3. **Signatures**: Create ECDSA signatures with proper DER encoding
4. **Witness Data**: Create witness stacks for SegWit transactions
5. **Complete Transaction**: Build a complete SegWit transaction

Each exercise is in its own directory with:
- `README.md`: Instructions specific to the exercise
- `template.py`: Template file where you'll write your code
- `test_exercise*.py`: Tests to verify your implementation

## Working Through the Exercises

1. Start with Exercise 1 and work through them in order
2. Read the exercise README for specific instructions
3. Complete the template file with your implementation
4. Run the tests to verify your solution

## Running Tests
```bash
# Run tests for a specific exercise
cd exercises/exercise1
python -m pytest test_exercise1.py -v

# Run all tests
python run_all_tests.py
```

## Resources
- [Bitcoin Developer Reference](https://developer.bitcoin.org/reference/)
- [BIP143 Specification](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)