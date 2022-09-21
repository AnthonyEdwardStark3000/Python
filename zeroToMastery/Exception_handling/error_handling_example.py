def sum(number1, number2):
    try:
        # return number1+number2
        return number1/number2
    except (TypeError, ZeroDivisionError) as happened_error:
        print(f'Plz enter a valid number \n{happened_error}')
    return 'Thank you'


print(sum(20, 0))
