def prime_numbers_generator(n):
    """ Function takes an integer argument n and populates a list with 
    prime numbers from 0 to n """   
    
    primes_list = []
    
    # reject string arguments
    if type(n) == str:
        return "String arguments are not allowed"
        
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
