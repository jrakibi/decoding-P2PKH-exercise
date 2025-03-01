import unittest
from template import sign

class TestSignatures(unittest.TestCase):
    
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
        
        # Check signature format
        self.assertTrue(signature.startswith(b'\x30'), "Signature does not start with DER sequence marker")
        self.assertEqual(signature[-1], 1, "Signature does not end with SIGHASH_ALL byte")
        
        # Test with another commitment
        commitment2 = bytes.fromhex(
            'a4696d36a7981fa74224547c2be8c5d9fb6c4e66cee9c0e2b265a740b8355e5c'
        )
        
        signature2 = sign(privkey, commitment2)
        
        # Just verify basic structure for second signature
        self.assertTrue(signature2.startswith(b'\x30'), "Second signature does not start with DER sequence marker")
        self.assertEqual(signature2[-1], 1, "Second signature does not end with SIGHASH_ALL byte")

if __name__ == '__main__':
    unittest.main() 