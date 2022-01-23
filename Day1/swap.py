# swapping the values of the two variables
a = int(input("Enter a:"))
b = int(input("Enter b:"))
a = a + b
# 10+20 a=30
b = a - b
# b= 30-20 =10
a = a - b
# 30-10 =20
a = str(a)
b = str(b)
print("a:"+a)
print("b:"+b)
