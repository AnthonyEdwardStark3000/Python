with open('my_file.txt', mode="a") as file:
    message = input("Enter something to enter into our file:")
    file.write(message)

with open('my_file.txt') as file:
    content = file.read()
    print(content)