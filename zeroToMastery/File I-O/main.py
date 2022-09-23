check_file = open('File I-O/dummy_file.txt')
print(check_file.read())
check_file.seek(0)
print(check_file.read())
print(check_file.readline())  # To read one line every time
print(check_file.readline())  # To read one line every time
print(check_file.readlines())  # To return every lines in the file as an list
check_file.close()  # For preventing the memory leaks
