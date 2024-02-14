import time


class Queue:
    ...


def process(item):
    time.sleep(0.5)
    print(f"{item} processed")


def handle_queue(queue: Queue):
    while len(queue) > 0:
        val = queue.pop(0)
        process(val)
        print(f"q: {queue}")


if __name__ == "__main__":
    started_at = time.time()

    vals = input(f"Users: ")
    q = Queue()
    for val in vals:
        q.append(val)
    print(f"q: {q}")

    handle_queue(q)

    print(f"q: {q}")

    print(f"Took {time.time() - started_at:.2f} seconds")
