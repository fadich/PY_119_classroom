x = 1
y = 2
z = 3


def func1():
    print("func1", x, y, z)


def func2():
    global x

    x += 3
    print("func2", x, y, z)


# func1()   //   func2()   //   x = 50

print("main", x, y, z)
