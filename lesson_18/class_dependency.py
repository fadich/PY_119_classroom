from typing import Union


class B:

    def meth(
        self,
        a=None,
        b: bool = False,
    ):
        """

        :param a:
        :type a: A

        :return:
        """
        print(a)


class A:

    def meth(self, b: B):
        print(b)


if __name__ == "__main__":
    a = A()
    b = B()

    a.meth(b)
    b.meth(a)
