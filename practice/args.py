def kargs(*number):
    print(f'checking the argument inside the function:{number}')
    print(type(number))
    return sum(number)
# print(kargs(1,2,3,4,5))    

def keyargs(*args, **kwargs):
    total = 0 
    for item in kwargs.values():
        total+= item
    return sum(args)+total    
print(keyargs(1,2,3,5,6,number1=10,number=20))    