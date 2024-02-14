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
def question6(n: int) -> int:
    while n > 1:
        time.sleep(0.01)
        n /= 2
        # print(n)
    return n


if __name__ == "__main__":
    question6(n=2)
    question6(n=10)
    question6(n=100)
    question6(n=1_000)
    question6(n=1_000_000)
    question6(n=1_000_000_000)
    question6(n=1_000_000_000_000)
    question6(n=1_000_000_000_000_000)
    question6(n=1_000_000_000_000_000_000)
    question6(n=1_000_000_000_000_000_000_000)
    question6(n=1_000_000_000_000_000_000_000_000_000_000_000_000_000)
