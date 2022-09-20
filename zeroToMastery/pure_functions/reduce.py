from functools import reduce


my_list = [1, 2, 3]


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))
# Here it assigns the accumulator argument acc to 0
# Then the item will be assigned with the value of the first element of the list.
# Then the val of variable acc will be changed to acc + item
