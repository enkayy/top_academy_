# # Задание 3
#
# class Airplane:
#
#     def __init__(self, model, max_passenger, passengers=0):
#         self.model = model
#         self.passengers = passengers
#         self.max_passenger = max_passenger
#
#     def __eq__(self, other):
#         """
#         Сравнение моделей
#         :param other:
#         :return:
#         """
#         if isinstance(other, Airplane):
#             return self.model == other.model
#         else:
#             return 'Сравнение невозможно'
#
#     def __add__(self, other):
#         """
#         Добавление пассажиров
#         :param other:
#         :return:
#         """
#         if isinstance(other, int):
#             return self.passengers + other
#         else:
#             return 'Сложение невозможно'
#
#     def __sub__(self, other):
#         if isinstance(other, int):
#             return self.passengers - other
#         else:
#             return 'Вычитание невозможно'
#
#     def __iadd__(self, other):
#         if isinstance(other, int):
#             self.passengers += other
#             return self
#         else:
#             return 'Сложение невозможно'
#
#     def __isub__(self, other):
#         if isinstance(other, int):
#             self.passengers -= other
#             return self
#         else:
#             return 'Вычитание невозможно'
#
#     def __gt__(self, other):
#         """
#         Сравнение максимального кол-ва пассажиров
#         :param other:
#         :return:
#         """
#         if isinstance(other, Airplane):
#             return self.max_passenger > other.max_passenger
#         else:
#             return 'Сравнение невозможно'
#
#     def __ge__(self, other):
#         if isinstance(other, Airplane):
#             return self.max_passenger >= other.max_passenger
#         else:
#             return 'Сравнение невозможно'
#
#     def __lt__(self, other):
#         if isinstance(other, Airplane):
#             return self.max_passenger < other.max_passenger
#         else:
#             return 'Сравнение невозможно'
#
#     def __le__(self, other):
#         if isinstance(other, Airplane):
#             return self.max_passenger <= other.max_passenger
#         else:
#             return 'Сравнение невозможно'
#
#
# airplane_1 = Airplane('Boeing 777', 120, 450)
# airplane_2 = Airplane('Boeing 777', 105, 500)
#
#
# print(airplane_1 == airplane_2)
#
# airplane_1 + 100
# print(airplane_1.passengers)
# airplane_1 += 1000
# print(airplane_1.passengers)
#
# print(airplane_1 >= airplane_2)


# # Задание 4
#
# class Flat:
#
#     def __init__(self, area, cost):
#         self.area = area
#         self.cost = cost
#
#     def __eq__(self, other):
#         if isinstance(other, Flat):
#             return self.area == other.area
#         else:
#             print('Сравнение невозможно')
#
#     def __ne__(self, other):
#         if isinstance(other, Flat):
#             return self.area != other.area
#         else:
#             print('Сравнение невозможно')
#
#     def __gt__(self, other):
#         if isinstance(other, Flat):
#             return self.cost > other.cost
#         else:
#             return 'Сравнение невозможно'
#
#     def __ge__(self, other):
#         if isinstance(other, Flat):
#             return self.cost >= other.cost
#         else:
#             return 'Сравнение невозможно'
#
#     def __lt__(self, other):
#         if isinstance(other, Flat):
#             return self.cost < other.cost
#         else:
#             return 'Сравнение невозможно'
#
#     def __le__(self, other):
#         if isinstance(other, Flat):
#             return self.cost <= other.cost
#         else:
#             return 'Сравнение невозможно'
#
#
# flat_1 = Flat(100, 30000)
# flat_2 = Flat(100, 30000)
#
# print(flat_1 == flat_2)
# print(flat_1 < flat_2)
