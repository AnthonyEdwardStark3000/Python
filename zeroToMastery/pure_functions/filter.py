my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_odd(numbers):
    return numbers % 2 != 0


print(list(filter(check_odd, my_list)))
