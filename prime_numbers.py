def prime_numbers_generator(n):
    """ Function takes an integer argument n and populates a list with 
    prime numbers from 0 to n """   
    
    primes_list = []
    
    # return false if n is 0 or 1
    if type(n) == int and n == 0 or n ==1:
        return False
    
    # reject string arguments
    if type(n) == str:
        return "String arguments are not allowed"
    
     # reject negative numbers   
    if type(n) == int and n < 0:
        return "Negative numbers are not allowed"
    
      # reject dictionary inputs   
    if type(n) is dict:
        return "Dictionary inputs are not allowed"
    
    # reject list inputs   
    if type(n) is list:
        return "List inputs are not allowed"
        
        
    # reject tuple inputs   
    if type(n) is tuple:
        return "Tuple inputs are not allowed"
    
    # reject float inputs   
    if type(n) is float:
        return "Floats are not allowed"
        
    i = 2
    while(i < n):
    
        j = 2
        while(j <= (i/j)):
        
            if not(i%j): 
                break
                
            j = j + 1
            
        if (j > i/j) : 
            primes_list.append(i)
            
        i = i + 1
        
        
        
        
        
        
def prime_output_checker(alist):

    """function returns true if output of prime_numbers_generator
       is prime numbers only"""
    
    for num in alist:
        if(num > 2):
            if num % 2 == 0:
                return False
    return True 
