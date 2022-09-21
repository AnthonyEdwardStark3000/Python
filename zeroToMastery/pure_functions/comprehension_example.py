numbers_entered = [1, 2, 3, 1, 2, 4]
duplicates = list(set([i for i in numbers_entered if numbers_entered.count(
    i) > 1]))
print(duplicates)
