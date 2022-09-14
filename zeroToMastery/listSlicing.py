shopping_cart = [
    'Book',
    'Computer',
    'Mac',
    'Money'
    ]
# print(shopping_cart[0::2])    
shopping_cart[0] = 'Let Us C'
# print(shopping_cart)

# Built-in methods of List 
basket = ['Noodles', 'Sauce', 'Rasamalai']
print(basket)
new_basket = basket.append('Nuts')
print(basket)
# Append should be done first then the assignment
print(f'check this : {new_basket}')

# Adding
basket.extend(['Rasagulla'])
print(basket)

#Removing
print('Removing the element from list')
basket.pop()
print(basket)
print('Removing the element based on index from list')
basket.pop(0)
print(basket)
print('Removing pariticular element based on its value or name')
basket.remove('Rasamalai')
print(basket)
basket.sort()
print(basket)
check = ['a','b','x','z','k','l','v','u']
check.sort()
check.reverse()
print(check)