while True:
    try:
        age = int(input('Enter your age :'))
        custom_division = 10/age
    except ValueError as error_happened:
        print(
            f'Sorry but you have entered an invalid age : \n{error_happened}')
    except ZeroDivisionError as error_happened:
        print(f'Sorry invalid entry \n {error_happened}')
    else:
        print('Done')
        break
    finally:
        print('Completed the execution of the program .')
