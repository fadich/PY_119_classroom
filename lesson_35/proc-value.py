import multiprocessing
import threading
import time


class A:
    a = "*" * 7


def worker(var: multiprocessing.Queue):
    print(f'process: {var.empty()}')
    var.put(1)
    print(f'process: {var.empty()}')
    time.sleep(2)
    # temp_var = {
    #     '1': 1,
    #     '2': 2,
    #     '3': 3,
    # }
    temp_var = A()
    print(f'process: {var.empty()}')
    var.put(temp_var)
    print(f'process: {var.empty()}')


if __name__ == "__main__":
    a = multiprocessing.Queue()
    proc = multiprocessing.Process(target=worker, args=(a, ))
    print(a.empty())
    proc.start()
    while True:
        if a.empty():
            # print('is empty')
            continue
        print(a.get())
        break

    print(a.empty())
    print(321)
    print(a.get().a)

    print(123)
    print(a.empty())
    proc.join()
