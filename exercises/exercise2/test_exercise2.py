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
        # Create test vectors based on BIP143
        version = bytes.fromhex("01000000")
        
        # Create inputs
        input1 = create_input(
            txid="9f96ade4b41d5433f4eda31e1738ec2b36f6e7d1420d94a6af99801a88f7f7ff",
            vout=0,
            sequence=b'\xee\xff\xff\xff'
        )
        
        input2 = create_input(
            txid="8ac60eb9575db5b2d987e29f301b5b819ea83a5c6579d282d189cc04b8e151ef",
            vout=1
        )
        
        # Create outpoint being spent (first 36 bytes of input)
        outpoint = input1[:36]
        
        # Create script code (P2PKH)
        script_code = bytes.fromhex("1976a9141d0f172a0ecb48aee1be1f2687d2963ae33f71a188ac")
        
        # Amount being spent (in satoshis)
        amount = (6*100000000 + 32454049).to_bytes(8, 'little')
        
        # Sequence number
        sequence = b'\xee\xff\xff\xff'
        
        # Create outputs
        output1 = create_output(
            amount=112340000,  # 1.1234 BTC
            script_pubkey=bytes.fromhex('1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac')
        )
        
        output2 = create_output(
            amount=223450000,  # 2.2345 BTC
            script_pubkey=bytes.fromhex('1976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac')
        )
        
        # Combine outputs
        outputs = output1 + output2
        
        # Locktime
        locktime = bytes.fromhex("11000000")
        
        # Sighash type
        sighash = bytes.fromhex("01000000")
        
        # Create prevouts (concatenate all outpoints)
        prev_outs = input1[:36] + input2[:36]
        
        # Create sequences (concatenate all sequences)
        sequences = input1[-4:] + input2[-4:]
        
        # Calculate digest
        digest = get_transaction_digest(
            version=version,
            prev_outs=prev_outs,
            sequences=sequences,
            output_to_spend=outpoint,
            script_code=script_code,
            amount=amount,
            sequence=sequence,
            outputs=outputs,
            locktime=locktime,
            sighash=sighash
        )
        
        # Expected digest from BIP143
        expected_digest = bytes.fromhex(
            'c37af31116d1b27caf68aae9e3ac82f1477929014d5b917657d0eb49478cb670'
        )
        
        self.assertEqual(digest, expected_digest, "Transaction digest incorrect")

if __name__ == '__main__':
    unittest.main() 