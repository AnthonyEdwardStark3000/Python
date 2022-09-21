while True:
    try:
        number = int(input('Enter a number :'))
        number = 100/number
        # raise Exception('Shut the program')
    # except Exception as error_occurred:
    #     print(f'New error occurred :{error_occurred}')
    except ZeroDivisionError as error_occurred:
        print(f'Stuck with a :{error_occurred}')
    else:
        print('Done')
        break
    finally:
        print('Thank you')
