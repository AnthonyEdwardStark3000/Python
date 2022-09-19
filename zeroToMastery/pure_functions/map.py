my_list = [1, 2, 3]


def multiply_by_2(num):
    return num*2


ans = map(multiply_by_2, my_list)

print(list(ans))
