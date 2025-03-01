import unittest
from template import dsha256, get_transaction_digest, create_input, create_output

class TestTransactionDigests(unittest.TestCase):
    
    def test_dsha256(self):
        """Test double SHA256 hash function"""
        # Test with empty string
        empty_hash = dsha256(b'')
        expected_empty = bytes.fromhex('5df6e0e2761359d30a8275058e299fcc0381534545f55cf43e41983f5d4c9456')
        self.assertEqual(empty_hash, expected_empty, "Double SHA256 of empty string incorrect")
        
        # Test with "hello world"
        hello_hash = dsha256(b'hello world')
        expected_hello = bytes.fromhex('bc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423')
        self.assertEqual(hello_hash, expected_hello, "Double SHA256 of 'hello world' incorrect")
    
    def test_transaction_digest(self):
        """Test BIP143 transaction digest calculation"""
        # Create inputs from BIP143 test vector
        input1 = create_input(
            txid="9f96ade4b41d5433f4eda31e1738ec2b36f6e7d1420d94a6af99801a88f7f7ff",
            vout=0,
            sequence=b'\xee\xff\xff\xff'
        )
        
        input2 = create_input(
            txid="8ac60eb9575db5b2d987e29f301b5b819ea83a5c6579d282d189cc04b8e151ef",
            vout=1
        )
        
        # Create outputs from BIP143 test vector
        output1 = create_output(
            amount=112340000,  # 1.1234 BTC
            script_pubkey=bytes.fromhex('1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac')
        )
        
        output2 = create_output(
            amount=223450000,  # 2.2345 BTC
            script_pubkey=bytes.fromhex('1976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac')
        )
        
        # Calculate digests
        hash_prevouts, hash_sequence, hash_outputs = get_transaction_digest(
            inputs=[input1, input2],
            outputs=[output1, output2]
        )
        
        # BIP143 test vector expected results
        expected_hashPrevouts = bytes.fromhex(
            '96b827c8483d4e9b96712b6713a7b68d6e8003a781feba36c31143470b4efd37'
        )
        expected_hashSequence = bytes.fromhex(
            '52b0a642eea2fb7ae638c36f6252b6750293dbe574a806984b8e4d8548339a3b'
        )
        expected_hashOutputs = bytes.fromhex(
            '863ef3e1a92afbfdb97f31ad0fc7683ee943e9abcf2501590ff8f6551f47e5e5'
        )
        
        self.assertEqual(hash_prevouts, expected_hashPrevouts, "hashPrevouts incorrect")
        self.assertEqual(hash_sequence, expected_hashSequence, "hashSequence incorrect")
        self.assertEqual(hash_outputs, expected_hashOutputs, "hashOutputs incorrect")

if __name__ == '__main__':
    unittest.main() 