from collections import Counter, defaultdict, OrderedDict
my_list = [1, 2, 3, 4, 5, 3, 2, 5, 7, 9, 3]
print(Counter(my_list))
my_name = 'Anthony Edward Stark'
print(Counter(my_name))

names_dict = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2})
print(names_dict['a'])
print(names_dict['z'])

name = OrderedDict()
name['first_name'] = 'Suresh'
name['last_name'] = 'Babu'

name2 = OrderedDict()
name2['last_name'] = 'Babu'
name2['first_name'] = 'Suresh'

print(f'Checking whether {name} is equal to {name2} :{name==name2}')

print(f'checking the same with regular dictionary')
check1 = {'a': 100, 'b': 200}
check2 = {'b': 200, 'a': 100}

print(f'Checking whether {check1} is equal to {check2} :{check1==check2}')
