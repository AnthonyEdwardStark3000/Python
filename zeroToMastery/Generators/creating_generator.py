def generator_creation(num):
    for i in range(num):
        yield i * 2


result = generator_creation(1)
print(next(result))
print(next(result))
