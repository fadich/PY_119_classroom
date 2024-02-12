import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        print(
            f"Function {func.__name__} took "
            f"{time.time() - started_at:.10f} seconds"
        )

        return result

    return wrapper


@timeit
def print_length(array: list):
    # time.sleep(2)
    print(f"List length is {len(array)}")


@timeit
def print_elements(array: list):
    for item in array:
        print(f"{item}", end="\r")
        # time.sleep(1)


@timeit
def multiply(array1: list):  # O(n) * O(n) = O(n^2)
    for item1 in array1:  # O(n)
        for item2 in array1:  # O(n)
            print(f"{item1} x {item2}", end="\r")


def two_time(array: list):  # O(n)
    time.sleep(100)

    for item in array:  # O(n)
        print(f"{item}", end="\r")

    print("And second time")

    for item in array:  # O(100) + O(n) + O(n) = O(n)
        print(f"{item}", end="\r")


if __name__ == "__main__":
    print("+++")
    print_length([])
    print_length([1, 2, 3])
    print_length([i for i in range(100)])
    print_length([i for i in range(1_000)])

    print("+++")
    print_elements([])
    print_elements([1, 2, 3])
    print_elements([i for i in range(1_000)])
    print_elements([i for i in range(10_000)])
    print_elements([i for i in range(100_000)])
    # print_elements([i for i in range(1_000_000)])
    # print_elements([i for i in range(10_000_000)])

    # multiply(
    #     ["Math", "English", "Literature"],
    #     ["Gandalf", "Frodo", "Sam", "Aragorn"]
    # )

    print("+++")
    multiply(
        [i for i in range(100)],  # O(n^2)
    )
    multiply(
        [i for i in range(1000)],  # O(n^2)
    )
    multiply(
        [i for i in range(10_000)],  # O(n^2)
    )
