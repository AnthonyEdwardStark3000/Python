# Dictionary in python is similar to JSON
programming_dictionary = {
    "Bug": "The one thing every programmer hates",
    "Function": "That one adithangi in every group",
    "Loop": "An Perfect example for suthudhu suthudhu indhaaru"
}

# Retrieving the value from the dictionary
bug = programming_dictionary["Bug"]
print(f"Bug can be defined as : {bug}")

# Retrieving the value from the dictionary
print(f"Loop can be defined as : {programming_dictionary['Loop']}")

# Adding new element to the dictionary
programming_dictionary["Data"] = "Raw Facts"

print(programming_dictionary)

# Empty dictionary

emptyDictionary = {}
print("\nDictionary\n")
print(emptyDictionary)
emptyDictionary["One"] = "Product number one"
emptyDictionary["Two"] = "Product number two"
emptyDictionary["Three"] = "Product number three"
print(emptyDictionary["One"])
print(emptyDictionary)

# Edit an item in the dictionary
emptyDictionary["Three"] = "Item number 3"
print(emptyDictionary)

# Looping through a dictionary
for key in emptyDictionary:
    print(emptyDictionary[key])

# Wiping the dictionary
emptyDictionary = {}
print(emptyDictionary)
