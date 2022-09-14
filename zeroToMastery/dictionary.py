example_dictionary = {
    'a': [1,2,3],
    'b': 'hello mr',
    'c': True,
}

print(example_dictionary)
print(example_dictionary['a'][2])
print(example_dictionary.get('name','Suresh')) 
print(example_dictionary)

user = dict(name = 'suresh', age='22')
print(user)

example_dictionary.update({'c':'False'})
print(example_dictionary)