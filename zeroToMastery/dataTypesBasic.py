# Escape Sequence 
from urllib.parse import quote_plus


weather = "It's Sunny"
print(weather)
weather = 'It\'s Sunny'
print(weather)
weather = 'It\\s Sunny'
print(weather)
escape_Sequence_Example = "\t It's \"Kind of \" sunny \n And I hope you have a nice Day !"
print(escape_Sequence_Example)


# String Formatting 
name = "Suresh"
age = 22
print(f"Hello {name} and you are {age} years old ")

print('HI {}. and How are you doing ?'.format('Mr.Stark'))

print('HI {username}. and How are you doing ? with your {project} language'.format(project="python",username='Mr.Stark'))

print(name[0:4:1])
print(name[::1])
print(name[-1])
startingAt = 0
endingAt = 5
increment = 1
print(name[startingAt:endingAt:increment])

# Built in methods
quote = 'Focus on the travel not on the destination'
print(quote.upper())
print(quote.lower())
print(quote.find('c'))
print(quote.replace('destination', 'Destination'))
# Example for string's immutability
print(quote)

birth_year = int(input('Enter your birth year :'))
print(f'You are {2022-birth_year} years old')
