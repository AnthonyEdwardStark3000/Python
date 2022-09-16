def highest_even(numbers):
    even = []
    for i in numbers:
        if i%2==0:
            even.append(i)
    # print(even)
    return max(even)        
print(highest_even([32,1,2,3,4,8,10,11,12,20,25]))    