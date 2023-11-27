# Задание 1

from math import pi


class Figure:
    line = 10
    color = "blue"

    def __init__(self, figure):
        self.figure = figure

    def get_area(self):
        return

    def get_figure_area(self):
        print(
            f"\nФигура: {self.figure}\n"
            f"Площадь: {self.get_area()}\n"
            f"Цвет: {self.color}"
        )


class Rectangle(Figure):
    def __init__(self, line_2):
        super(Rectangle, self).__init__("Прямоугольник")
        self.line_2 = line_2

    def get_area(self):
        area = self.line_2 * self.line
        return area


class Circle(Figure):
    color = "yellow"

    def __init__(self):
        super(Circle, self).__init__("Круг")

    def get_area(self):
        area = self.line**2 * pi
        return round(area, 1)


class RightTriangle(Figure):
    def __init__(self, line_2):
        super().__init__("Прямоугольный треугольник")
        self.line_2 = line_2

    def get_area(self):
        area = (self.line_2 * self.line) / 2
        return area


class Trapezoid(Figure):
    color = "red"

    def __init__(self, line_2, height):
        self.line_2 = line_2
        self.height = height
        super().__init__("Трапеция")

    def get_area(self):
        area = (self.line_2 + self.line) * (self.height / 2)
        return area


rectangle = Rectangle(10)
rectangle.get_figure_area()

circle = Circle()
circle.get_figure_area()

right_triangle = RightTriangle(10)
right_triangle.get_figure_area()

trapezoid = Trapezoid(10, 15)
trapezoid.get_figure_area()
