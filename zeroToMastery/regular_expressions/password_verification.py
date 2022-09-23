import re
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'hjsadbasld86836$9l'
a = pattern.fullmatch(password)
print(f'I would like to say that the password is : {a}')
