def do_num_plus_five(number):
    print('num + 5')
    try:
        return int(number) + 5
    except TypeError as error:
        return error
