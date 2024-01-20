
def gen():
    print("== 0 ==")
    yield 1
    print("== 1 ==")
    yield 2
    print("== 2 ==")
    yield 3
    print("== 3 ==")
    yield 4
    print("== 4 ==")


def list_iter(list_var):
    index = 0
    while len(list_var):
        # try:
        yield list_var[index]
#         except IndexError:
#             break
        index += 1


if __name__ == "__main__":
    # x = gen()
    # for val in x:
    #     print(f"val = {val}")

    x = list_iter([1, 2, 3])
    print(x)
    while True:
        try:
            val = next(x)
        except StopIteration:
            break

        print(f"val = {val}")
