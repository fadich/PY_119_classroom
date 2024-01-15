

class A(object):
    counter = 0
    self = None

    def __init__(self, value):
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("NEW")
        print(f"cls.self: {A.self}")
        if cls.self is not None:
            return A.self

        cls.self = super().__new__(cls)  # <-------------

        print(f"cls.self: {A.self}")
        cls.counter += 1

        return cls.self

    # def __del__(self):
    #     print("Del")

    # def __str__(self):
    #     print("Str method called")
    #
    #     return repr(self)
    #
    # def __repr__(self):
    #     print("Repr method called")
    #
    #     return "<A object>"

    # def __eq__(self, other):
    #     if not isinstance(other, A):
    #         raise TypeError(f"Cannot compare <class A> and {type(other)}")
    #     print("EQ")
    #     return True

    # def __gt__(self, other):
    #     return bool()
    #
    # def __ge__(self, other):
    #     return bool()

    def __len__(self):
        print("LEN")
        return 123

    def __int__(self):
        print("INT")

    def __float__(self):
        print("Float")

    def __bool__(self):
        print("Bool")
        return True

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     return 1

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __call__(self, *args, **kwargs):
        print("Called")

    def __add__(self, other):
        pass

    # def __setattr__(self, key, value):
    #     print("__setattr__", key, value)
    #     setattr(self, key, value)


if __name__ == "__main__":
    a = A(1)
    b = A(6)

    # print(a.value)
    a.asdfg = 123

    # print(a + 2)  # a.__add__(2)

    # str(a)
    # repr(a)
    # print(a)
    # len(a)

    # print(a == b)  # a.__eq__(b)
    # print(1 == a)  # a.__eq__(b)
    # print(a > b)  # a.__gt__(b)
    # print(a >= b)  # a.__ge__(b)
    # if 1 in a:  # 1 in [1, 2, 3]
    #     print("123")

    # hash(a)
    # s = {a, a, b}
    # print(s)
    # print(a in s)
    #
    # print(hash(a))
    # print(hash(b))

    # print(hash("9999"))
    # print(hash("9999"))
    #
    # l1 = (1, 2, 3, 4)
    # l2 = (1, 2, 3, 4)
    #
    # print(l1 == l2)

    # a()
