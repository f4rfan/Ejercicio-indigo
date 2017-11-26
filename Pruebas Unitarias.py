import unittest
import largest_palindrome_product
import largest_product_in_a_series


class PalindromeTest(unittest.TestCase):
    
    def test_palindrome(self):
        respuesta = [101101,707,143]
        self.assertEqual(largest_palindrome_product.pruebas( 1, 101101), respuesta)


class ProductTest(unittest.TestCase):
    
    def test_product(self):
        self.assertEqual(largest_product_in_a_series.pruebas( 1, 10, 5, 3675356291), 3150)
        
if __name__ == "__main__":
    unittest.main()
