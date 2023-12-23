from m1 import module_1_func

print(__file__)
print(__name__)


def module_2_func():
    print("M2 func")


if __name__ == "__main__":
    print("m2: This is an entry point")
