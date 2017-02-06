import unittest

from prime_numbers import prime_numbers_generator


class ten_test_cases(unittest.TestCase):

    """Class defines methods to test prime_numbers_generator 
    function from prime_numbers.py"""    
    
    # test that string arguments are not allowed
    def test_no_strings_allowed(self):
        self.assertEqual(prime_numbers_generator("astring"),"String arguments are not allowed")
            
            
if __name__ == '__main__':      
    unittest.main()      