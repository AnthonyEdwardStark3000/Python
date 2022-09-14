sample_tuple = (1,2,3,4,5)
print(sample_tuple)

# Checking for a presence of value
print(100 in sample_tuple)
print(1 in sample_tuple)

# Using tuple as a key in dictionary
sample_user ={
    ('name','age'):['Suresh',22],
    'greet': 'Hello'
}

print(sample_user[('name','age')])

tuple_example = (100,200,300,400,500)
new_tuple_extracted = tuple_example[1:3]
print(new_tuple_extracted)

a,b,c,*other = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(a)
print(other)