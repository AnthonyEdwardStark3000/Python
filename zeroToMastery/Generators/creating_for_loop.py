def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # To check the next element in the memory location
            print(next(iterator), end='\t')
            # print(iterator) # To check the memory location
        except StopIteration as error_happened:
            print(f'\nThe execution stops as {error_happened} occurred')
            break


special_for_loop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
