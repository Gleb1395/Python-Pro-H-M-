import math


class Cycle:
    x_const = 10
    y_const = 10
    radius_const = 5

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def contains(self) -> bool:
        distance = math.sqrt((self.x - self.x_const)**2 + (self.y - self.y_const)**2)
        return distance <= self.radius_const

point_1 = Cycle(2,9)
print(point_1.contains())
