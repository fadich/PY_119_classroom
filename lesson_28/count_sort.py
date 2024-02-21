from typing import List

a = [1, 2, 3, 1, 2, 2, 1, 3, 1, 2, 1, 2, 3, 2, 3, 1, 2, 9]


def count_sort(lst: List[int]):
    # counter = [0, 0, 0, 0]
    counter = {
        1: 0,
        2: 0,
        3: 0,
    }
    for item in lst:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1

    return counter


if __name__ == "__main__":
    cs = count_sort(a)
    print(cs)
    for i in cs.keys():
        print(f"{i}" * cs[i], end="")
