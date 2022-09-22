print(__name__)


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as zero:
        print(f'Sorry {zero} error occurs.')
