
class A:

    def __init__(self):
        self.a = 1  # public
        self._b = 2  # _protected
        self.__c = 3  # __private

    def public(self):
        print("public")

    def _protected(self):
        print("_protected")

    def __private(self):
        print("__private")


class B(A):

    def test(self):
        self.public()
        self._protected()
        self._B__private()  # Error!


if __name__ == "__main__":
    a = A()
    a.public()
    a._protected()

    print(a._A__private())  # a.__private()

    b = B()
    b.test()
