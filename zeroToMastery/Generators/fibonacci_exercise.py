def fibonacci(num):
    first = 0
    second = 1
    for i in range(num):
        yield first
        temp = first
        first = second
        second = temp + first


fibonacci_numbers = fibonacci(10)
for number in fibonacci_numbers:
    print(number)
