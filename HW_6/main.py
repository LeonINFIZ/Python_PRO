"""
1. Створити клас Circle(x,y,radius). Додати метод contains.
 Цей метод приймає екземпляр класу Point(x,y). Цей метод має повертати
 True or False. Якшо точка в колі то True якшо поза колом то False.

2. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).

Triangle - треба створити клас

3. Сцена, включить видос
"""

import math

class Shape: #class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi*self.radius**2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width


    def square(self):
        return self.width*self.height


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
        return (self.width*self.height)*self.angle

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


try:
    triangle = Triangle(3, 4, 10)
    print("Площадь:", triangle.square())
except ValueError as e:
    print("Ошибка:", e)


scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(t)
scene.add_figure(t1)

print(scene.total_square())
