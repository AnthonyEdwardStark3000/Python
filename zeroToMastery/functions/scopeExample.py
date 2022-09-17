a = 10 # Global
def confusion(number):
    print(f"Variable with local scope :{number}") # 300
    a = 20 
    return a # 20

# print(confusion(300)) # Functions # print 20

# 300
# 20

a=1
def function2():
    a = 5 # Local scope
    return a # Local scope

# print(f'Output of function 2 :{a}') # 1
# print(f'Value returned from function 2 :{function2()}') # 5

number = 100
def a_function():
    return number

# print(number)        

    love = 100

    def parent_scope():
        love = 3000
        def local_scope():
            return love
        return local_scope()    

    # print(f"Mr.stark says Love you {parent_scope()}")

# Built in function
def calling_function():
    def built_in_function():
        return sum  
    return built_in_function()

print(calling_function)        