
g = 2
h = 3


def my_func(a, b, c, d):
    """My function's doc"""

    e = 1
    f = 2

    return a + b + c + d


# print(func(1, 2, 3))

print(repr(my_func.__doc__))
print(my_func.__code__.co_argcount)


a = [1, 2, 3]
# print(dir(a))
# print(a.__dir__())
print(a.__class__)
print(my_func.__class__)

print("".__class__)
print(1.0.__class__)
print(int(1).__class__)
