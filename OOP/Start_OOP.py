import math


class Circle:
    def __init__(self, x: int = 10, y: int = 10, radius: int = 5):
        self.x = x
        self.y = y
        self.radius = radius

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def contains(self, circle: Circle) -> bool:
        distance = math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2)
        return distance <= circle.radius

circle_1 = Circle(10, 10, 5)
point_1 = Point(11, 8)
print(point_1.contains(circle_1))
