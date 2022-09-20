from functools import reduce
my_list = [1, 2, 3, 4, 5]

print(list(map(lambda item: item*2, my_list)))

print(
    f'Performing filter operation :{list(filter(lambda item: item %2 !=0,my_list))}')

print(
    f'Performing reduce operation :{reduce(lambda acc, item: acc + item, my_list)}')
