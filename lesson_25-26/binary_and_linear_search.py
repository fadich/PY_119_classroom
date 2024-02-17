from typing import (
    Any,
    List,
)

lst = ["gandalf", "frodo", "aragorn", "gimli"]


def in_(lst: List[Any], item: Any) -> bool:
    # return any(l == item for l in lst)
    for l in lst:
        if l == item:
            return True
    return False


def bin_find(lst: List[Any], item: Any) -> bool:
    if len(lst) == 1:
        return lst[0] == item
    middle = len(lst) // 2
    if lst[middle] == item:
        return True
    if lst[middle] < item:
        return bin_find(lst[middle:], item)
    # else: lst[middle] > item
    return bin_find(lst[0:middle], item)


def bin_find_cycle(lst: List[Any], item: Any) -> bool:
    while True:
        if len(lst) == 1:
            return lst[0] == item
        middle = len(lst) // 2
        if lst[middle] < item:
            lst = lst[middle:]
        elif lst[middle] > item:
            lst = lst[0:middle]
        else:
            return True


if __name__ == '__main__':
    print(in_(lst, "aragorn"))
    print(bin_find(sorted(lst), "gimli"))
    print(bin_find_cycle(sorted(lst), ""))
