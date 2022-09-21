from time import time


def performance(function):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = function(*args, **kwargs)
        t2 = time()
        print(f'Time taken to complete this execution is {t2-t1} ms')
        return result
    return wrapper


@performance
def multiplication():
    for i in range(0, 1000):
        print(i*5
              )


multiplication()
