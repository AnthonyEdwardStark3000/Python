def repeat():
    print("Greet")
# repeat()    

def greetUser(gender,name='Undefined'):
    print(f"Hello {gender}{name}") 
# greetUser(gender="Mr.")    

def sum(number1, number2):
    sum = number1+number2
    return sum
print(sum(10,20))    

def sum_ans(number1, number2):
    def another_function(n1,n2):
        return n1+n2
    return another_function(number1, number2)

total = (sum_ans(10,15))
print(total)     

def check():
    '''
    This is created for check purpose.
    '''
check()    
print(check.__doc__)