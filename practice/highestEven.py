def highest_even(li):
    evens = []
    for numbers in li:
        if numbers % 2==0:
            evens.append(numbers)
        return max(evens)    
print(f'The highest number among the entered is:{highest_even([100,2,3,4,8,11])}')    