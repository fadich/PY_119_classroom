
def func():
    x = 9
    x += 1

    return x


def gen():
    x = 9
    x += 1

    print("== 0 ==")
    yield x
    print("== 1 ==")
    yield "second value"
    print("== 2 ==")
    yield "third value value"
    print("== 3 ==")


if __name__ == "__main__":
    g = gen()
    print(next(g))  # == 0 ==
    print("Something")
    print(next(g))  # == 1 ==
    print(next(g))  # == 2 ==
    print(next(g))  # == 3 == | ERROR!
