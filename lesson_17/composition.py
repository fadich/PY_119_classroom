from typing import (
    List,
    Optional,
)


class Furniture:
    pass


class Wall:
    pass


class Room:

    def __init__(
        self,
        walls: List[Wall],
        furniture: Optional[List[Furniture]] = None,
    ):
        self.walls = walls

        if furniture is None:
            furniture = []
        self.furniture = furniture


room = Room(
    walls=[
        Wall(),
        Wall(),
        Wall(),
        Wall(),
    ],
)

sofa = Furniture()
table = Furniture()
chair = Furniture()

room.furniture.append(table)
room.furniture.remove(table)

del room

###############################################################################


class Eater:

    def eat(self):
        raise NotImplementedError()


class Character(Eater):

    def eat(self):
        ...


class Robot(Eater):

    def __init__(self):
        self.c = Character()

    def eat(self):
        return self.c.eat()


r = Robot()
r.eat()
r.c.eat()


print(isinstance(r, Character))  # False
print(isinstance(r, Eater))  # True
