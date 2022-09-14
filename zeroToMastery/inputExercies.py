name = input('Enter your Name :')
password = input('Enter your Password :')
password_length = len(password)
hidden_password = '*' *password_length
print(f'''{name} Your password {hidden_password} is {password_length} characters long''')