from typing import Any


class HashTableExample:

    def __init__(self):
        self.storage = [
            None, None, None, None, None,
            None, None, None, None, None,
        ]

    def add(self, item: Any):
        hash_value = self.get_hash(item)  # 0..9
        if self.storage[hash_value] is None:
            self.storage[hash_value] = item
        else:
            self.storage[hash_value] = [
                self.storage[hash_value],
                item,
            ]

    def find(self, item: Any) -> bool:
        hash_value = self.get_hash(item)  # 0..9
        if isinstance(self.storage[hash_value], list):
            return item in self.storage[hash_value]

        return self.storage[hash_value] == item

    @classmethod
    def get_hash(cls, item: Any) -> int:  # 0..9
        return len(str(item)) % 10


if __name__ == "__main__":
    hte = HashTableExample()
    print(hte.storage)
    print(hte.find("Gimli"))  # None

    print("===")

    hte.add("Aragorn")
    hte.add("Gimli")
    hte.add("Frodo")
    print(hte.storage)
    print(hte.find("Gimli"))  # None
