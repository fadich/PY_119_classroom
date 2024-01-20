from collections.abc import (
    Iterator,
)
from random import random


class MyIterator(Iterator):  # class MyIterator:

    def __iter__(self):
        return iter(range(5))

    def __next__(self):
        if random() < 0.05:
            raise StopIteration()

        return 1


class ListIterator(Iterator):

    def __init__(self, some_list):
        self._list = some_list
        self._index = 0

    def __next__(self):
        try:
            return self._list[self._index]
        except IndexError:
            raise StopIteration()
        finally:
            self._index += 1

    def reset(self):
        self._index = 0


if __name__ == "__main__":
    big_list = [x for x in range(10)]
    my_list_iterator = ListIterator(big_list)

    for index, value in enumerate(my_list_iterator):
        print(f"[{index}] value = {value}")

    my_list_iterator.reset()

    for index, value in enumerate(my_list_iterator):
        print(f"[{index}] value = {value}")

    print(f"=== my_iterator ===")
    my_iterator = MyIterator()
    for index, value in enumerate(my_iterator):
        print(f"[{index}] value = {value}")
