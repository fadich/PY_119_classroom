from copy import deepcopy


class Store:

    def __init__(self):
        self._income = 0
        self._store = []

    def add_product(self, name: str, price: float):
        self._income += price

    def get_income(self):
        return self._income

    def set_income(self, value: float):
        self._income = value

    def get_store(self):
        return deepcopy(self._store)


if __name__ == "__main__":
    store = Store()
    store.add_product(
        name="Apple",
        price=99.99,
    )

    print(store.get_income())

    st = store.get_store()
    st.append(123)


    print(store._store)
