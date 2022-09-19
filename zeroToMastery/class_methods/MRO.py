class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(
    f'For checking the Order of the class inherited and Executed : {D.mro()}')
