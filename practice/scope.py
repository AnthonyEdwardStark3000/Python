# a = 10
# def confusion(number):
#     print(f"Variable with local scope :{number}")
#     a = 20
#     return a

# print(confusion(300))

count = 1
def counter():
    global count
    count += 1
    return count
print(counter())    
print(counter())    
print(counter())    
print(counter())    