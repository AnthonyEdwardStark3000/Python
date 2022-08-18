from multiprocessing.reduction import duplicate


some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for character in some_list:
    if some_list.count(character) >1:
        if character not in duplicates:
            duplicates.append(character)
print(duplicates)        