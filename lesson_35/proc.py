from multiprocessing import Process


def target():
    print(123)


if __name__ == "__main__":
    proc = Process(target=target)
    proc.start()
    proc.join()

