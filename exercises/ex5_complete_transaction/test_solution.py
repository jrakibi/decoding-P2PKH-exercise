import unittest
from template import assemble_transaction, int_to_little_endian, varint

class TestCompleteTransaction(unittest.TestCase):
    
    def test_assemble_transaction(self):
        """Test assembling a complete SegWit transaction"""
        # Create mock inputs (simplified for testing)
        input1 = bytes.fromhex(
            "fff7f7881a8099afa6940d42d1e7f6362bec38171ea3edf433541db4e4ad969f"  # txid (little-endian)
            "00000000"  # vout
            "00"        # script length (empty script)
            "eeffffff"  # sequence
        )
        
        input2 = bytes.fromhex(
            "ef51e1b804cc89d182d279655c3aa89e815b1b309fe287d9b2b55d57b90ec68a"  # txid (little-endian)
            "01000000"  # vout
            "00"        # script length (empty script)
            "ffffffff"  # sequence
        )
        
        # Create mock outputs
        output1 = bytes.fromhex(
            "202cb20600000000"  # amount (1.1234 BTC)
            "1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac"  # P2PKH script
        )
        
        output2 = bytes.fromhex(
            "9093510d00000000"  # amount (2.2345 BTC)
            "1976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac"  # P2PKH script
        )
        
        # Create mock witness data
        witness1 = bytes.fromhex(
            "02"  # Number of witness items
            "47"  # Signature length (71 bytes)
            "304402203609e17b84f6a7d30c80bfa610b5b4542f32a8a0d5447a12fb1366d7f01cc44a"
            "0220573a954c4518331561406f90300e8f3358f51928d43c212a8caed02de67eebee01"
            "21"  # Public key length (33 bytes)
            "025476c2e83188368da1ff3e292e7acafcdb3566bb0ad253f62fc70f07aeee6357"
        )
        
        witness2 = bytes.fromhex(
            "00"  # Empty witness
        )
        
        # Assemble transaction
        tx = assemble_transaction(
            version=1,
            inputs=[input1, input2],
            outputs=[output1, output2],
            witnesses=[witness1, witness2],
            locktime=0x11000000
        )
        
        # Expected transaction from BIP143 example (with some modifications for our test)
        expected = bytes.fromhex(
            "01000000" +  # version
            "0001" +      # marker & flag
            "02" +        # input count
            "fff7f7881a8099afa6940d42d1e7f6362bec38171ea3edf433541db4e4ad969f00000000" +
            "00eeffffff" +
            "ef51e1b804cc89d182d279655c3aa89e815b1b309fe287d9b2b55d57b90ec68a01000000" +
            "00ffffffff" +
            "02" +        # output count
            "202cb206000000001976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac" +
            "9093510d000000001976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac" +
            # witness data
            "02" +        # number of witness items for input 1
            "47" +        # length of first witness item
            "304402203609e17b84f6a7d30c80bfa610b5b4542f32a8a0d5447a12fb1366d7f01cc44a" +
            "0220573a954c4518331561406f90300e8f3358f51928d43c212a8caed02de67eebee01" +
            "21" +        # length of second witness item
            "025476c2e83188368da1ff3e292e7acafcdb3566bb0ad253f62fc70f07aeee6357" +
            "00" +        # empty witness for input 2
            "00001100"    # locktime
        )
        
        self.assertEqual(tx, expected, "Transaction does not match expected output")
        
        # Test with different number of inputs/outputs
        tx2 = assemble_transaction(
            version=2,
            inputs=[input1],
            outputs=[output1],
            witnesses=[witness1],
            locktime=0
        )
        
        # Check basic structure
        self.assertEqual(tx2[:4], bytes.fromhex("02000000"), "Version incorrect")
        self.assertEqual(tx2[4:6], bytes.fromhex("0001"), "Marker and flag incorrect")
        self.assertEqual(tx2[6:7], bytes.fromhex("01"), "Input count incorrect")
        
        # Check witness data is present
        self.assertIn(witness1, tx2, "Witness data missing")
        
        # Check locktime
        self.assertEqual(tx2[-4:], bytes.fromhex("00000000"), "Locktime incorrect")

if __name__ == '__main__':
    unittest.main() 