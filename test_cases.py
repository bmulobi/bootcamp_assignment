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
        
      # return false if n is 0
    def test_false_if_zero(self):
        self.assertFalse(prime_numbers_generator(0))        
        
    # return false if n is 1
    def test_false_if_one(self):
        self.assertFalse(prime_numbers_generator(1)) 
        
    # test for float inputs
    def test_no_floats(self):
        self.assertEqual(prime_numbers_generator(99.999),"Floats are not allowed")  
        
        
    # test for overflow
    def test_no_overflow(self):
        self.assertEqual(prime_numbers_generator(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999),"Overflow")     
            
            
if __name__ == '__main__':      
    unittest.main()      
