set_numbers = {1,2,2,3,4,5,6,7,8,9,10,11}
print(set_numbers)

example_list = [1,2,2,3,4,5,6,7,8,9]
print(f'\nOriginal List :{example_list}')
new_set  = set(example_list)
print(f'Set version :{new_set}')

print(type(new_set))

# Important Set methods
print(set_numbers.difference(new_set))
print(set_numbers.discard(8))
print(set_numbers)