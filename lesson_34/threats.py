import threading

import sys

x = 1
y = 2
z = 3


def func1():
    print(threading.current_thread().name, x, y, z)


def func2():
    print(threading.current_thread().name, x, y, z)


thr1 = threading.Thread(name="function_1", target=func1)
thr2 = threading.Thread(target=func2)


if __name__ == "__main__":
    thr1.start()
    thr2.start()

    print(threading.current_thread().name, x, y, z)
