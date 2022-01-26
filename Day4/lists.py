alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
]
print("\n ******************** Before Appending ******************** \n")
for i in alphabets:
    print(i)
alphabets.append("Check Append")
print("\n ******************** After Appending ******************** \n")
for i in alphabets:
    print(i)
print("\n ******************** Adding Additional list ********************  \n")
alphabets.extend(["Some", "Few", "Survive"])
for i in alphabets:
    print(i)
