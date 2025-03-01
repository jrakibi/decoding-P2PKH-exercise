import unittest
from template import (
    sign, get_p2wpkh_witness, assemble_transaction,
    create_input, create_output, get_commitment_hash
)

class TestBitcoinTransactions(unittest.TestCase):
    
    def test_signature(self):
        """Test signature generation against BIP143 test vector"""
        # Private key from BIP143 test vector
        privkey = bytes.fromhex(
            '619c335025c7f4012e556c2a58b2506e30b8511b53ade95ea316fd8c3286feb9'
        )
        
        # Commitment hash from BIP143
        commitment = bytes.fromhex(
            'c37af31116d1b27caf68aae9e3ac82f1477929014d5b917657d0eb49478cb670'
        )
        
        # Generate signature
        signature = sign(privkey, commitment)
        
        # Expected signature from BIP143
        expected_sig = bytes.fromhex(
            '304402203609e17b84f6a7d30c80bfa610b5b4542f32a8a0d5447a12fb1366d7f01cc44a' +
            '0220573a954c4518331561406f90300e8f3358f51928d43c212a8caed02de67eebee01'
        )
        
        self.assertEqual(signature, expected_sig, "Signature does not match BIP143 test vector")
    
    def test_witness_stack(self):
        """Test witness stack generation against BIP143 test vector"""
        # Private key from BIP143
        privkey = bytes.fromhex(
            '619c335025c7f4012e556c2a58b2506e30b8511b53ade95ea316fd8c3286feb9'
        )
        
        # Commitment hash from BIP143
        commitment = bytes.fromhex(
            'c37af31116d1b27caf68aae9e3ac82f1477929014d5b917657d0eb49478cb670'
        )
        
        # Generate witness stack
        witness = get_p2wpkh_witness(privkey, commitment)
        
        # Expected witness data from BIP143 (broken down for clarity)
        expected_witness = (
            b'\x02' +                    # Number of witness items
            b'\x47' +                    # Signature length (71 bytes)
            bytes.fromhex(                # DER signature + SIGHASH_ALL
                '304402203609e17b84f6a7d30c80bfa610b5b4542f32a8a0d5447a12fb1366d7f01cc44a' +
                '0220573a954c4518331561406f90300e8f3358f51928d43c212a8caed02de67eebee01'
            ) +
            b'\x21' +                    # Public key length (33 bytes)
            bytes.fromhex(                # Compressed public key
                '025476c2e83188368da1ff3e292e7acafcdb3566bb0ad253f62fc70f07aeee6357'
            )
        )
        
        self.assertEqual(witness, expected_witness, "Witness stack does not match BIP143 test vector")
    
    def test_final_transaction(self):
        """Test final transaction assembly with BIP143 test vector"""
        
        # First input with its signature script
        input1 = create_input(
            txid="9f96ade4b41d5433f4eda31e1738ec2b36f6e7d1420d94a6af99801a88f7f7ff",
            vout=0,
            sequence=b'\xee\xff\xff\xff',
            script_sig=bytes.fromhex(
                '4830450221008b9d1dc26ba6a9cb62127b02742fa9d754cd3bebf337f7a55d114c8e5cdd30be' +
                '022040529b194ba3f9281a99f2b1c0a19c0489bc22ede944ccf4ecbab4cc618ef3ed01'
            )
        )
        
        # Second input (P2WPKH)
        input2 = create_input(
            txid="8ac60eb9575db5b2d987e29f301b5b819ea83a5c6579d282d189cc04b8e151ef",
            vout=1,
            sequence=b'\xff\xff\xff\xff'
        )
        
        # Create outputs
        output1 = create_output(
            amount=112340000,  # 1.1234 BTC
            script_pubkey=bytes.fromhex('1976a9148280b37df378db99f66f85c95a783a76ac7a6d5988ac')
        )
        
        output2 = create_output(
            amount=223450000,  # 2.2345 BTC
            script_pubkey=bytes.fromhex('1976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac')
        )
        
        # Get witness data for second input (P2WPKH)
        privkey = bytes.fromhex('619c335025c7f4012e556c2a58b2506e30b8511b53ade95ea316fd8c3286feb9')
        outpoint = input2[:36]  # First 36 bytes are outpoint
        scriptcode = bytes.fromhex('1976a9141d0f172a0ecb48aee1be1f2687d2963ae33f71a188ac')
        
        commitment = get_commitment_hash(
            outpoint=outpoint,
            scriptcode=scriptcode,
            value=600000000,  # 6 BTC
            outputs=[output1, output2],
            all_inputs=[input1, input2]
        )
        
        # Create witnesses
        witness1 = b'\x00'  # Empty witness for first input
        witness2 = get_p2wpkh_witness(privkey, commitment)
        
        # Assemble final transaction
        final_tx = assemble_transaction(
            inputs=[input1, input2],
            outputs=[output1, output2],
            witnesses=[witness1, witness2]
        )
        
        # Expected final transaction from BIP143
        expected = bytes.fromhex(
            '01000000000102fff7f7881a8099afa6940d42d1e7f6362bec38171ea3edf433541db4e4ad969f' +
            '00000000494830450221008b9d1dc26ba6a9cb62127b02742fa9d754cd3bebf337f7a55d114c8' +
            'e5cdd30be022040529b194ba3f9281a99f2b1c0a19c0489bc22ede944ccf4ecbab4cc618ef3ed' +
            '01eeffffffef51e1b804cc89d182d279655c3aa89e815b1b309fe287d9b2b55d57b90ec68a010' +
            '0000000ffffffff02202cb206000000001976a9148280b37df378db99f66f85c95a783a76ac7a' +
            '6d5988ac9093510d000000001976a9143bde42dbee7e4dbe6a21b2d50ce2f0167faa815988ac0' +
            '00247304402203609e17b84f6a7d30c80bfa610b5b4542f32a8a0d5447a12fb1366d7f01cc44a' +
            '0220573a954c4518331561406f90300e8f3358f51928d43c212a8caed02de67eebee012102547' +
            '6c2e83188368da1ff3e292e7acafcdb3566bb0ad253f62fc70f07aeee635711000000'
        )
        
        self.assertEqual(final_tx, expected, "Final transaction does not match BIP143 test vector")

if __name__ == '__main__':
    unittest.main() 