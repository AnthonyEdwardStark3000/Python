# read write append in a file
with open('File I-O/dummy_file.txt', mode='r+') as my_file:
    # To read and write r+ is used
    message = '\nThe Truth is all strength is within us and a true effort never dies'
    result = my_file.write(message)
    print(result)
    print(my_file.readlines())  

# To add text to the end of the file without modifying the existing content in it
# The append mode can be used

with open('File I-O/dummy_file.txt', mode='a') as add_file:
    additional_message = 'And your capacities are far more greater than you think'
    result = add_file.write(additional_message)
    print(result)
    print(add_file.readlines())
