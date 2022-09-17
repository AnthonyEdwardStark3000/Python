a = 10

def check_function():
    global a
    a = 100
    print(f'Inside the function :{a}')
    return a
print(f'The value returned from the function :{check_function()}')
print(f'The value of the global scoped variable :{a}')