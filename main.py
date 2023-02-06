# String handling
message = "Happy Birthday"
print(f'Length:{len(message)}') # returned length is printed
print(f'Index:{message.find("#")}') # returned bool value is printed
print(f'Index:{message.count("a")}') # returned count of value is printed
name="ram"
quote='"peace"'
msg = name+message
print(quote)

#invoking a method
print(name.upper()) # returned string is printed
print(name.lower())
print(name.capitalize())
print(name.replace('a','k'))
print(f'is completely a alphabet + numbers:{message.isalpha()}')
print(f'is completely a digit{message.isdigit()}')
print(f'is completely is in lower case{message.islower()}')
print(f'is completely is in upper case{message.isupper()}')
print(message*10)