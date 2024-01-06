def calc_sum(*args):
    return sum(args)


def main():
    ...


print("MODULE 1")
print("module1.py name:", __name__)


if __name__ == "__main__":
    main()
    print("1 + 2 =", calc_sum(1, 2))
    print("2 + 2 =", calc_sum(2, 2))
    print("6 + 2 + 3 =", calc_sum(6, 2, 3))
