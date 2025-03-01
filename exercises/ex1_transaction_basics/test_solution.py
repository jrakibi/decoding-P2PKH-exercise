import unittest
from template import create_input, create_output, create_basic_tx

class TestTransactionBasics(unittest.TestCase):
    
    def test_create_input(self):
        """Test creating a transaction input"""
        # Create input with default sequence
        input1 = create_input(
            txid="9f96ade4b41d5433f4eda31e1738ec2b36f6e7d1420d94a6af99801a88f7f7ff",
            vout=0
        )
        
        # Expected serialized input
        expected = bytes.fromhex(
            "fff7f7881a8099afa6940d42d1e7f6362bec38171ea3edf433541db4e4ad969f"  # txid (little-endian)
            "00000000"  # vout
            "00"        # script length (empty script)
            "ffffffff"  # sequence
        )
        
        self.assertEqual(input1, expected, "Input serialization incorrect")
        
        # Create input with custom script_sig and sequence
        script_sig = bytes.fromhex("48304502210084d96818b9825f4f891562458e0a943e5a2eac147e32698ba4951ea8f1c79ee7022060fbda12c87682ac3a58f1f0e7eee2b5b973df1a7bc99c903f19c0b0e693a1f701")
        input2 = create_input(
            txid="8ac60eb9575db5b2d987e29f301b5b819ea83a5c6579d282d189cc04b8e151ef",
            vout=1,
            script_sig=script_sig,
            sequence=b'\xee\xff\xff\xff'
        )
        
        # Check length is correct (36 bytes for outpoint + script length + script + sequence)
        expected_length = 32 + 4 + 1 + len(script_sig) + 4
        self.assertEqual(len(input2), expected_length, "Input length incorrect")
        
        # Check txid and vout are correct
        self.assertEqual(input2[:32], bytes.fromhex("ef51e1b804cc89d182d279655c3aa89e815b1b309fe287d9b2b55d57b90ec68a"), "txid incorrect")
        self.assertEqual(input2[32:36], bytes.fromhex("01000000"), "vout incorrect")
        
        # Check sequence is correct
        self.assertEqual(input2[-4:], b'\xee\xff\xff\xff', "Sequence incorrect")
    
    def test_create_output(self):
        """Test creating a transaction output"""
        # Create a P2PKH output
        script_pubkey = bytes.fromhex("1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac")
        output = create_output(
            amount=112340000,  # 1.1234 BTC
            script_pubkey=script_pubkey
        )
        
        # Expected serialized output
        expected = bytes.fromhex(
            "202cb20600000000"  # amount (little-endian)
            "1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac"  # script_pubkey
        )
        
        self.assertEqual(output, expected, "Output serialization incorrect")
        
        # Check amount is correct
        self.assertEqual(output[:8], bytes.fromhex("202cb20600000000"), "Amount incorrect")
        
        # Check script_pubkey is correct
        self.assertEqual(output[8:], script_pubkey, "ScriptPubKey incorrect")
    
    def test_basic_transaction(self):
        """Test creating a basic transaction"""
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
        
        # Create outputs
        output1 = create_output(
            amount=112340000,  # 1.1234 BTC
            script_pubkey=bytes.fromhex("1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac")
        )
        
        output2 = create_output(
            amount=223450000,  # 2.2345 BTC
            script_pubkey=bytes.fromhex("1976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac")
        )
        
        # Create transaction
        tx = create_basic_tx(
            version=1,
            inputs=[input1, input2],
            outputs=[output1, output2],
            locktime=0x11,
            segwit=False
        )
        
        # Expected transaction from BIP143 example
        expected = bytes.fromhex(
            "0100000002fff7f7881a8099afa6940d42d1e7f6362bec38171ea3edf433541db4e4ad969f"
            "0000000000eeffffffef51e1b804cc89d182d279655c3aa89e815b1b309fe287d9b2b55d57"
            "b90ec68a0100000000ffffffff02202cb206000000001976a9148280b37df378db99f66f85"
            "c95a783a76ac7a6d5988ac9093510d000000001976a9143bde42dbee7e4dbe6a21b2d50ce"
            "2f0167faa815988ac11000000"
        )
        
        self.assertEqual(tx, expected, "Transaction does not match expected output")

if __name__ == '__main__':
    unittest.main() 