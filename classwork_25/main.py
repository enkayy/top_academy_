# --- Паттерны ---
# MVC
# Model - моделька
# View - для пользователя, общение пользователя с базой/кодом
# controller - связь между моделью и вью, решает что делать с запросом пользователя

# class Pizza:
#
#     def __init__(self, name):
#         self.name = name
#         self.toppings = []
#
#     def add_topping(self, topping):
#         self.toppings.append(topping)
#
#     def get_description(self):
#
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#         self.status = 'In Progress'
#
#     def add_pizza(self):
#
#
#     def calculate_total(self):
#         return 100 * len(self.pizzas)
#
#     def complete_order(self):
#         self.status = 'Complete'
#         return f'Order completed. Total cost: {self.calculate_total()}'
#
#
# class Payment:
#
#     @staticmethod
#
#
# class Report:
#
#     @staticmethod
#     def generate_sales_report(orders):


# Задача по работе с дробями

# from fractions import Fraction
# import unittest  # стандартный модуль для тестирования
#
#
# class FractionCalculator:
#     def __init__(self, numerator, denominator):
#         self.fraction = Fraction(numerator, denominator)
#
#     def add(self, other):
#         return self.fraction + other.fraction
#
#     def sub(self, other):
#         return self.fraction - other.fraction
#
#     def mult(self, other):
#         return self.fraction * other.fraction
#
#     def dev(self, other):
#         return self.fraction / other.fraction
#
#
# class TestFractionCalculator(unittest.TestCase):
#
#     def setUp(self):
#         self.frac1 = FractionCalculator(1, 2)
#         self.frac2 = FractionCalculator(1, 4)
#
#     def test_add(self):
#
#         self.assertEqual(self.frac1.add(self.frac2), Fraction(3, 4))  # тест ttd
#
#     def test_sub(self):
#         self.assertEqual(self.frac1.sub(self.frac2), Fraction(1, 4))
#
#     def test_mult(self):
#         self.assertEqual(self.frac1.mult(self.frac1), Fraction(1, 8))
#
#     def test_del(self):
#         self.assertEqual(self.frac1.dev(self.frac2), Fraction(2, 1))
#
#
#
# if  __name__ == "__main":
#     unittest.main


import unittest


class Calculator:
    def __init__(self, num):
        self.num1 = num

    def add(self, other):
        return self.num1 + other.num1

    def sub(self, other):
        return self.num1 - other.num1

    def mult(self, other):
        return self.num1 * other.num1

    def div(self, other):
        return self.num1 / other.num1

    def max(self, other):
        return max(self.num1, other.num1)

    def min(self, other):
        return min(self.num1, other.num1)

    def percent(self, other):
        return (self.num1 / other.num1) * 100

    def degree(self, other):
        return self.num1**other.num1


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.num1 = Calculator(5)
        self.num2 = Calculator(10)
        self.num3 = Calculator(2)

    def test_add(self):
        self.assertEqual(self.num1.add(self.num2), 15)

    def test_subtract(self):
        self.assertEqual(self.num2.sub(self.num1), 5)

    def test_mult(self):
        self.assertEqual(self.num1.mult(self.num2), 50)

    def test_div(self):
        self.assertEqual(self.num2.div(self.num1), 2)

    def test_max(self):
        self.assertEqual(self.num1.max(self.num2), 10)

    def test_min(self):
        self.assertEqual(self.num1.min(self.num2), 5)

    def test_percent(self):
        self.assertEqual(self.num1.percent(self.num2), 50)

    def test_degree(self):
        self.assertEqual(self.num1.degree(self.num3), 25)
