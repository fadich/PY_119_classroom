import time


def process(item):
    time.sleep(0.5)
    print(f"{item} processed")


def handle_stack(stack):
    while len(stack) > 0:
        val = stack.pop()
        process(val)
        print(f"q: {stack}")


if __name__ == "__main__":
    started_at = time.time()

    vals = input(f"Users: ")
    s = list(vals)
    print(f"q: {s}")

    handle_stack(s)

    print(f"q: {s}")

    print(f"Took {time.time() - started_at:.2f} seconds")


# LIFO - Stack (FILO)
# FIFO - Queue
# LIFO + FIFO - Dequeue
