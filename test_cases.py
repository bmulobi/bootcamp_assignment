import unittest

from prime_numbers import prime_numbers_generator,prime_output_checker


class ten_test_cases(unittest.TestCase):

    """Class defines methods to test prime_numbers_generator 
    function from prime_numbers.py"""    
    
    # test that string arguments are not allowed
    def test_no_strings_allowed(self):
        self.assertEqual(prime_numbers_generator("astring"),"String arguments are not allowed")
        
   # test output has prime numbers only    
    def test_output_is_prime_only(self):
        self.assertTrue(prime_output_checker(prime_numbers_generator(100)))   
        
    # reject negative numbers    
    def test_no_negative_numbers(self):
        self.assertEqual(prime_numbers_generator(-20),"Negative numbers are not allowed")     
        
    # reject dictionary inputs
    def test_no_dictionaries_allowed(self):
        self.assertEqual(prime_numbers_generator({'a':1}),"Dictionary inputs are not allowed")   
        
   # reject list inputs
    def test_no_lists_allowed(self):
        self.assertEqual(prime_numbers_generator([1,2,7]),"List inputs are not allowed")    
        
        
     # reject tuple inputs
    def test_no_tuples_allowed(self):
        self.assertEqual(prime_numbers_generator((2,5,1,6)),"Tuple inputs are not allowed")      
            
            
if __name__ == '__main__':      
    unittest.main()      
