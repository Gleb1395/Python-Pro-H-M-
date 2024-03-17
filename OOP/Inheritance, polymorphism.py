import math


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def contains(self, point: Point) -> bool:
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height

    def contains(self, point: Point) -> bool:
        coord_x = self.x - (self.width / 2) <= point.x <= self.x + (self.width / 2)
        coord_y = self.y - (self.height / 2) <= point.y <= self.y + (self.height / 2)
        if coord_x == True and coord_y == True:
            return True
        else:
            return False


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.height * self.width * math.sin(self.angle)

    def contains(self, point: Point) -> bool:
        angle_rad = math.radians(self.angle)
        rotated_x = (point.x - self.x) * math.cos(angle_rad) - (point.y - self.y) * math.sin(angle_rad)
        rotated_y = (point.x - self.x) * math.cos(angle_rad) + (point.y - self.y) * math.sin(angle_rad)
        coord_x = rotated_x - (self.width / 2) <= point.x <= rotated_x + (self.width / 2)
        coord_y = rotated_y - (self.height / 2) <= point.y <= rotated_y + (self.height / 2)
        if coord_x == True and coord_y == True:
            return True
        else:
            return False


class Triangle(Shape):
    def __init__(self, x, y, side1, side2, side3):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return area

    def triangle_coords(self):
        x_a = self.x - self.side1 / 2
        y_a = self.y - math.sqrt(3) * self.side1 / 2

        x_b = self.x + self.side1 / 2
        y_b = self.y - math.sqrt(3) * self.side1 / 2

        x_c = self.x
        y_c = self.y + math.sqrt(3) * self.side1 / 2

        return x_a, y_a, x_b, y_b, x_c, y_c

    def contains(self, point: Point) -> bool:
        x1, y1, x2, y2, x3, y3 = self.triangle_coords()
        x, y = point.x, point.y
        denom = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denom
        beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denom
        gamma = 1.0 - alpha - beta
        return alpha > 0 and beta > 0 and gamma > 0


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)

p1 = Parallelogram(1, 2, 20, 30, 45)
str(p1)

t1 = Triangle(5, 5, 10, 10, 10)
t2 = Triangle(4, 3, 10, 11, 17)


scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(t1)
scene.add_figure(t2)
print(scene.total_square())

# print(scene.total_square())
point_1 = Point(1, 1)
print(t1.contains(point_1))