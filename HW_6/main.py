import math
from math import floor


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def contains(self, point: Point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2) <= self.radius

    def __str__(self):
        return f'Circle({self.x}, {self.y}, {self.radius}) with Square: {round(self.square(), 1)}'


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return abs(self.width * self.height)

    def __str__(self):
        return f'Rectangle({self.x}, {self.y}, {self.height}, {self.width}) with Square: {round(self.square(), 1)}'


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        return f'Parallelogram({self.width}, {self.height}, {self.angle}) with Square: {round(self.square(), 1)}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.width * self.height * math.sin(math.radians(self.angle))


class Triangle(Shape):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def is_valid(self):
        return (self.x + self.y > self.z and
                self.x + self.z > self.y and
                self.y + self.z > self.x)

    def perimeter(self):
        return self.x + self.y + self.z

    def square(self):
        S = self.perimeter() / 2
        return math.sqrt(S * (S - self.x) * (S - self.y) * (S - self.z))

    def __str__(self):
        return f'Triangle({self.x}, {self.y}, {self.z}) with Square: {round(self.square(), 1)}'


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        if figure:
            self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        result = (f"\n============== SCENE ==============\n"
                  f"Total Square: {round(self.total_square(), 1)}\n\n")

        for figure in self._figures:
            result += str(figure) + "\n"

        result += "==================================="

        return result


def create_triangle(triangle: Triangle):
    try:
        if not triangle.is_valid():
            raise ValueError("Invalid triangle")
        else:
            return triangle
    except ValueError as e:
        print("ERROR:", e)
        return None


############### RECTANGLE ###############

r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

############### RECTANGLE ###############

############### CIRCLE ###############

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

### POINT ###
c2 = Circle(0, 0, 5)
point = Point(3, 4)

if c2.contains(point):
    print(f"{point} is inside {c2}")
else:
    print(f"{point} is not inside {c2}")

c3 = Circle(3, 2, 5)
point = Point(6, 10)

if c3.contains(point):
    print(f"{point} is inside {c3}")
else:
    print(f"{point} is not inside {c3}")
### POINT ###

############### CIRCLE ###############

############### PARALLELOGRAM ###############

p = Parallelogram(1, 2, 20, 30, 45)
p1 = Parallelogram(1, 2, 20, 30, 45)
p2 = Parallelogram(0, 0, 5, 8, 30)

############### PARALLELOGRAM ###############


scene = Scene()

scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)

scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(c2)
scene.add_figure(c3)

scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(p2)

t1 = create_triangle(Triangle(6, 4, 3))   # OK
t2 = create_triangle(Triangle(6, 4, 2))   # ERROR
t3 = create_triangle(Triangle(10, 8, 6))  # OK

scene.add_figure(t1)
scene.add_figure(t2)  # Will not be added
scene.add_figure(t3)

print(scene)
