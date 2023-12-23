from dt import datetime

print(__file__)
print(__name__)


def module_1_func():
    from m2 import module_2_func

    print("M1 func")
    module_2_func()


if __name__ == "__main__":
    print("m1: This is an entry point")
    print(123)
    module_1_func()
