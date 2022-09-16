# Default return value 
def addition(number1, number2):
    number1+ number2
# print(f"The default return value of a function:{addition(100,50)}")

# The value that user return 
def sum_ans(number1, number2):
    def second_function(n1,n2):
        return n1+ n2
    return second_function(number1,number2)

# print(f"The value returned using the return keyword :{sum_ans(100,40)}")
a = 10
# print(type(a))

def checkReturn(number):
    for i in range(number,0,-1):
        if i <= 5:
            return "Thank you."
        else:
            print(i)
print(checkReturn(7))            