import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_entered = 'suresh@gmail.com'

a = pattern.match(email_entered)
print(f'After validation your email approval :{a}')
