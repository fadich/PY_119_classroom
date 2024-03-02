import time
import multiprocessing


def make_calculations():
    x = 0
    while x < 10_000_000:
        x += 1


if __name__ == "__main__":
    start_at = time.time()
    for u in range(10):
        print(u)
        make_calculations()
    end_at = time.time()
    total_time = end_at - start_at
    print(total_time)

    start_at = time.time()

    procs = []

    for u in range(10):
        proc = multiprocessing.Process(target=make_calculations)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
        print(proc.name)

    end_at = time.time()

    total_time = end_at - start_at
    print(total_time)
