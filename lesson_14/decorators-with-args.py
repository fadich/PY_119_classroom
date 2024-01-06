from functools import wraps
from typing import Callable


def wrap_function(number):
    def decorator(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)

            print("#" * 30)
            print(f"{func.__name__}({args}, {kwargs}) = {val}")
            print("#" * 30)

            return val

        return wrapper

    return decorator

    # print("wrap_function CALLED")


@wrap_function  # square = wrap_function(square)
@wrap_function(10)
def square(number: float):
    return number ** 2


@wrap_function  # sqrt = wrap_function(sqrt)
def sqrt(number: float):
    return number ** 0.5


@wrap_function  # say_hello = wrap_function(say_hello)
def return_hello():
    return "Hello!"


square(11)
sqrt(number=1)

print("====")

square(10)
sqrt(10)

print(sqrt.__name__)
print(square.__name__)
