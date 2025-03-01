import unittest
from template import sum_list

class TestSumList(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)
        
    def test_single_element(self):
        self.assertEqual(sum_list([5]), 5)
        
    def test_multiple_elements(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        
    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3]), -6)
        
    def test_mixed_numbers(self):
        self.assertEqual(sum_list([-1, 2, -3, 4]), 2)
        
    def test_float_numbers(self):
        self.assertAlmostEqual(sum_list([1.5, 2.5]), 4.0)

if __name__ == '__main__':
    unittest.main() 