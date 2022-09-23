try:
    with open('File I-O/dummy_file.txt', mode='r') as my_file:
        message = my_file.read()
        print(message)
except FileNotFoundError as fnof:
    print(f'Please check your location {fnof}')
except IOError as io:
    print(f'Please check your location {io}')
else:
    print('Done with operation and now closing the file')
