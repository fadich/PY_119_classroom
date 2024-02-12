import random
import abc


class Apple(abc.ABC):
    SIZE_MEDIUM = "medium"
    SIZE_LARGE = "large"
    COLORS = (
        "red",
        "yellow",
        "green",
        "white",
    )

    number = 0

    def __init__(self, size: str = SIZE_MEDIUM):
        self._size = size
        self._color = self.__class__.generate_color()
        self.__class__.number += 1

    def is_medium(self) -> bool:
        # return self._size == Apple.SIZE_MEDIUM
        return self._size == self.SIZE_MEDIUM

    @classmethod
    @abc.abstractmethod
    def generate_color(cls) -> str:
        return random.choice(cls.COLORS)

    def __del__(self):
        self.number -= 1

    @property
    @abc.abstractmethod
    def asd(self):
        return


class Jonathan(Apple):
    COLORS = (
        "red",
    )


class Golden(Apple):
    COLORS = (
        "yellow",
    )


class WhitePouring(Apple):
    COLORS = (
        "green",
        "white",
    )


if __name__ == "__main__":
    jon = Jonathan()
    jon2 = Jonathan()
    gol = Golden()
    bn = WhitePouring()

    print(Jonathan.generate_color())

    print(Apple.number)
    print(Golden.number)
    print(Jonathan.number)
    print(jon.number)
