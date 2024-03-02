import threading


l = list(range(10_000))


def write(file: str, lst, my_e: threading.Event, their_e: threading.Event):
    for i in lst:
        print(f"{threading.current_thread().name}: Wait for their event")
        their_e.wait()

        print(f"{threading.current_thread().name}: clearing their event")
        their_e.clear()

        print(f"{threading.current_thread().name}: writhing")
        with open(file, "a") as f:
            f.write(f"{threading.current_thread().name}: {i}\n")

        print(f"{threading.current_thread().name}: setting my event")
        my_e.set()


file = "example.txt"
with open(file, "w") as f:
    f.write("")

lock = threading.Lock()
e1 = threading.Event()
e2 = threading.Event()
# write("example.txt", l)
thr1 = threading.Thread(target=write, args=(file, l, e1, e2))
thr2 = threading.Thread(target=write, args=(file, l, e2, e1))
thr1.start()
thr2.start()
e1.set()
thr1.join()
thr2.join()


""" ======= EXAMPLE ======= """

def target2():
    for _ in range(100_000):
        sleep(0.001)
        if event.isset():
            return

    event2.set()


def target(event):
    while not event.isset():
        try:
            event2.wait(timeout=0.001)
            break
        except TimeoutError:
            continue


try:
    while True:
        ...

except KeyboardInterrupt:
    event.set()
