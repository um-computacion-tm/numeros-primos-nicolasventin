import unittest

from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime_1 (self):
        result = is_prime(1)
        self.assertEqual(result,False)

    def test_prime_2 (self):
        result = is_prime(2)
        self.assertEqual(result,True)
    
    def test_prime_3 (self):
        result = is_prime(3)
        self.assertEqual(result,True)
    
    def test_prime_4 (self):
        result = is_prime(4)
        self.assertEqual(result,False)
    
    def test_prime_5 (self):
        result = is_prime(5)
        self.assertEqual(result,True)
    
    def test_prime_6 (self):
        result = is_prime(6)
        self.assertEqual(result,False)
    
    def test_prime_7 (self):
        result = is_prime(7)
        self.assertEqual(result,True)
    
    def test_prime_8 (self):
        result = is_prime(8)
        self.assertEqual(result,False)
    
    def test_prime_9(self):
        result = is_prime(9)
        self.assertEqual(result,False)
        
    def test_prime_91(self):
        result = is_prime(91)
        self.assertEqual(result,False)
        
    def test_prime_357897 (self):
        result = is_prime(357897)
        self.assertEqual(result,False)

    def test_prime_973547 (self):
        result = is_prime(973547)
        self.assertEqual(result,True)

if __name__ == "__main__":
    unittest.main()