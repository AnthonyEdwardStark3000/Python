import re

message = 'check this using regular expressions and print to print the result'
string_to_search = re.compile('print')
object_returned = string_to_search.search(message)
print(object_returned)
a = string_to_search.findall(message)
print(f'findall : {a}')
b = string_to_search.search(message)
print(f'search : {b}')
c = string_to_search.fullmatch(message)
print(f'fullmatch : {c}')
c = string_to_search.match(message)
print(f'match : {c}')
