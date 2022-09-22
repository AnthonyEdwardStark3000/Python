def fibonacci(num):
    first = 0
    second = 1
    result = []
    for i in range(num):
        result.append(first)
        temp = first
        first = second
        second = temp + first
    return result


fibonacci_numbers = fibonacci(10)
print(fibonacci_numbers)
