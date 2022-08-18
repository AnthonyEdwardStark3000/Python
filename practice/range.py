print(range(100))
for i in range(1,10):
    print(i)
for i in range(1,10,3):
    print(i)    
for i in range(10,1,-3):
    print(i)    
print("Enumerate :")

for i, char in enumerate('Mr.Stark'):
    print(i, ":" ,char)      

print("while loop")

a =10
while a>0 and a<15:
    print(a)
    a+=1

print("else block in while :") 
  i = 0 
while i<5:
    print(i)
    i+=1
else:
    print("Thank you")  

print("pass")
for i in range(1,3):
    print(i)
    pass
    print("Hello")