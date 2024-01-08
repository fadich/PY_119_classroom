# Built-in (Python)
print()


# Global (module)
a = 1
print(a)
from random import *


# Local (function)
def func():
    b = 2


# ====
print("=" * 30)
x = 1
y = 3


def my_func():
    x = 20
    def inner():
        global y

        nonlocal x

        y = y + 1
        x += 1

        return x + y

    return inner


my_callable = my_func()
print(my_callable())
print(y)
