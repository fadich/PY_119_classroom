
class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def get_highest(self, p2: "Point"):
        if self.y > p2.y:
            return self
        else:
            return p2

    def calc_distance(self, p2: "Point") -> float:
        return 0.0


print("POINT 1")
point1 = Point(x=1.0, y=0.0)
print(point1.x)
print(point1.y)
print(point1.get_coords())

print("POINT 2")
point2 = Point(x=2, y=6)
print(point2.x)
print(point2.y)
print(point2.get_coords())


def get_highest(p1: Point, p2: "Point"):
    if p1.y > p2.y:
        return p1
    else:
        return p2


point1.calc_distance(point2)


p1 = (1, 2)
p2 = (5, 3)
