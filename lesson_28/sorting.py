from typing import List

a = [1, 5, 9, 2, 1, 0, 6, 5, -1, 5, 50, 123]

c = ["elephant", "dog", "guitar", "car", "Jacket", "flower", "banana", "hat",
     "ice cream", "apple"]


def bobble_sort(lst: List[str]):
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]

    return lst


def insert_(lst: List[str]):  # Selection
    length = len(lst)
    for i in range(length - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

    return lst


if __name__ == "__main__":
    print(insert_(lst=a))
    print(bobble_sort(
        lst=[
            "Frodo",
            "gandalf",
            "aRagorn",
        ] + c
    ))
