from typing import Callable


def wrap_function(func: Callable):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)

        print("#" * 30)
        print(f"{func.__name__}({args}, {kwargs}) = {val}")
        print("#" * 30)

        return val

    # print("wrap_function CALLED")
    return wrapper


@wrap_function  # square = wrap_function(square)
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
