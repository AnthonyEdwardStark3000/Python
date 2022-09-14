is_old = True
is_licensed = False

if(is_old and is_licensed):
    print('You can drive a car.')
elif is_old:
    print('Apply for license')
else:
    print('Grow first')        
print('End of the Loop')    

# Truthy and falsy
name = 'check'
if name:
    print('Hello Mr.')
else:
    print('Hi')        

#   Ternary operator
is_Friend = False
message = "Allowed" if is_Friend else "Not Allowed"
print(f'Messaging me is :{message}')