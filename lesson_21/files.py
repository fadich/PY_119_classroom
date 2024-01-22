import time
from typing import Optional

filepath = "./my_file.txt"

# with open(filepath, "w") as file:
#     pass
"""
with ... [as variable]:
    ...  # code
"""


class Timer:

    def __init__(self):
        self._start_time: Optional[float] = None
        self._end_time: Optional[float] = None

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def delta(self) -> float:
        return self.end_time - self.start_time

    def __enter__(self) -> "Timer":
        print("__enter__")

        self._start_time = time.time()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")

        self._end_time = time.time()

        # print(self.delta)
        # print(exc_type, exc_val, exc_tb)


if __name__ == "__main__":
    t = Timer()
    with t as timer:
        input("Press [ENTER]")
        ...
        ...

    print(f"Time: {t.delta}")
