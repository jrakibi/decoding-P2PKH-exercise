import unittest
from template import get_pub_from_priv, get_p2wpkh_witness, sign

class TestWitnessData(unittest.TestCase):
    
    def test_get_pub_from_priv(self):
        """Test public key derivation from private key"""
        # Private key from BIP143
        privkey = bytes.fromhex(
            '619c335025c7f4012e556c2a58b2506e30b8511b53ade95ea316fd8c3286feb9'
        )
        
        # Generate public key
        pubkey = get_pub_from_priv(privkey)
        
        # Expected public key from BIP143
        expected_pubkey = bytes.fromhex(
            '025476c2e83188368da1ff3e292e7acafcdb3566bb0ad253f62fc70f07aeee6357'
        )
        
        self.assertEqual(pubkey, expected_pubkey, "Public key does not match expected value")
        
        # Check format
        self.assertEqual(len(pubkey), 33, "Compressed public key should be 33 bytes")
        self.assertTrue(pubkey.startswith(b'\x02') or pubkey.startswith(b'\x03'), 
                        "Compressed public key should start with 0x02 or 0x03")
    
    def test_p2wpkh_witness(self):
        """Test P2WPKH witness stack creation"""
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
        
        # Check structure
        self.assertEqual(witness[0], 2, "Witness should have 2 items for P2WPKH")
        
        # Check signature length
        sig_len = witness[1]
        self.assertEqual(sig_len, len(witness[2:2+sig_len]), "Signature length incorrect")
        
        # Check public key length
        pubkey_offset = 2 + sig_len
        pubkey_len = witness[pubkey_offset]
        self.assertEqual(pubkey_len, len(witness[pubkey_offset+1:pubkey_offset+1+pubkey_len]), 
                         "Public key length incorrect")

if __name__ == '__main__':
    unittest.main() 