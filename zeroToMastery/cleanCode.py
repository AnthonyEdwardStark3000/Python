def unclean_code(number):
    '''
    creating this code just to demonstrate how to write a
    clean code.
    '''
    def is_odd_or_even(n):
        if(n%2==0):
            return True
        elif (n%2!=0):
            return False
    return is_odd_or_even(number)
Number =10
print(f"The number {Number} is even :{unclean_code(Number)}")                


def clean_code(number):
    '''
    Turning the above coded unclean code to cleaner one. 
    '''
    def is_odd_or_even(n):
        return n%2 == 0    
    return is_odd_or_even(number)        
print(f"The clean code says Number {Number} is even : {clean_code(Number)}")    