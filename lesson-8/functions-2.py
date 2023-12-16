from copy import copy

names = ["Gandalf"]


def hello(n=None):
    if n is None:
        n = []

    print(f"Inside 1: {id(n)}", n)
    n.append("1231231")
    print(f"Inside 2: {id(n)}", n)


print(f"Before: {id(names)}", names)
hello()
hello()
hello()
print(f"After: {id(names)}", names)


def a(a=1, b=2, c=3, d=4):
    pass


l = [1, 2, 3, 4]
a(*l)  # a(1, 2, 3, 4)


d = {
    "b": 1,
    "c": 10,
}
a(**d)  # a(b=1, c=10)

d = {
    "b": 1,
    "c": 10,
}
a(*d)  # a("b", "c")
a(*d.values())  # a(1, 10)


def func(a, b, *args, c=5, d=6, **kwargs):
    pass


a = 1
