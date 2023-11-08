# --- Объектно-ориентированное программирование ---

# название класса пишется с большой буквы

# import time
# import random
#
#
# class Vehicle:
#     # это метод, которые используется в классе
#     def __init__(self, name: str, weight: float, hp: int, max_speed: int):  # в этот метод передаются свойства экземпляра
#         # __метод__, который доступен в классе всегда (нижние подчеркивания)
#         self.name = name
#         self.weight = weight
#         self.hp = hp
#         self.__wheel_count = 4  # общие свойства экземпляров можно задать прямо в классе, будет задаваться ко всему
#         # двойное нижнее перед свойством означает, что значение нельзя использовать извне, но в классе можно
#         # два нижних - нельзя менять, одно нижнее - не желательно менять
#         self.start_fuel = 12
#         self.max_speed = max_speed
#         self.possible_barrier = ['Дерево', 'Столб', 'Обрыв']
#
#     # def output_info(self):
#     #     print(f'Информация о машине:\n\n'
#     #           f'Название: {self.name}\n'
#     #           f'Масса: {self.weight}\n'
#     #           f'HP: {self.hp}\n')
#
#     # @staticmethod
#     # def refuel(liters: float):  # статичный метод, который не использует атрибуты экземпляра класса (self)
#     #     print(f'Машина заправлена на {liters} литров')
#
#     def refuel(self, liters: float):
#         print(f'Машина заправлена на {liters} литров, теперь в баке {self.start_fuel + liters} литров')
#         self.start_fuel += liters
#
#     def drive(self):
#         self.start_fuel -= 10
#         if self.start_fuel > 0:
#             print(f'Литров топлива осталось: {self.start_fuel}')
#         else:
#             print('В машине закончилось топливо!!')
#
#     # def boost(self):  # мой способ
#     #     start = time.time()
#     #     if self.max_speed >= 100:
#     #         time.sleep(3.5)
#     #         print(f'Разгон до 100: {time.time() - start} секунд')
#     #         if self.max_speed >= 200:
#     #             time.sleep(1.5)
#     #             print(f'Разгон до 200: {time.time() - start} секунд')
#     #             if self.max_speed >= 300:
#     #                 time.sleep(1)
#     #                 print(f'Разгон до 300: {time.time() - start} секунд')
#     #         time.sleep(1)
#     #         print(f'Разгон до максимальной {self.max_speed} км/ч {time.time() - start} секунд')
#
#     def boost(self):  # способ Никиты
#         speed = self.max_speed / 3.6
#         start = time.time()
#         for i in range(0, self.max_speed, 20):
#             if random.randint(1, 10) == 1:
#                 print(f'Вы встретили препятствие {random.choice(self.possible_barrier)} при загоне')
#                 return
#             time.sleep(1)
#             print(f'Текущая время {i / speed} cекунд достигла скорости {i}')
#         print(f'Машина {self.name} достигла максимально скорости')
#
#     # магический метод срабатывает при вызове функции, а обычный метод нужно вызвать
#     def __str__(self):  # магический метод. Срабатывает, когда пытаемся вывести в консоль через print
#         return (f'Информация о машине:\n'
#                 f'Название: {self.name}\n'
#                 f'Масса: {self.weight}\n'
#                 f'HP: {self.hp}\n'
#                 f'Колеса: {self.__wheel_count}\n')


# создаем экземпляр/объект для класса

# vehicle_1 = Vehicle('Audi', 1700, 180, 230)  # можно передать так
# vehicle_2 = Vehicle(name='BMW', weight=2200, hp=575, max_speed=356)
# vehicle_1 = Vehicle(name='Audi A4', weight=1800, hp=180)  # можно по именам

# print(vehicle_1.name)  # можно обратиться к конкретному свойству
# vehicle_1.output_info()  # так достается информация из класса
# vehicle_2.output_info()  # сущность одна, но объекты разные

# vehicle_1.max_speed = 240  # можно задавать свойства вне экземпляра, но назначается только к одному экземпляру
# print(vehicle_2)
# print(vehicle_1.max_speed)

# print(vehicle_1)
# print(vehicle_2)

# vehicle_1.refuel(35.4)
# print(vehicle_1.start_fuel)
#
# vehicle_1.drive()
# vehicle_1.drive()
# vehicle_1.drive()
# vehicle_1.drive()
# vehicle_1.drive()
#
# vehicle_1.boost()
# vehicle_2.boost()

# class Human:
#
#     def __init__(self, fullname: str, birth_date: str, tel: str, city: str, country: str):
#         # пишем класс для сеттеров и геттеров
#         self.fullname = fullname
#         self.birth_date = birth_date
#         self.tel = tel
#         self.city = city
#         self.country = country
#
#     def set_fullname(self, value):
#         self.fullname = value
#
#     def get_fullname(self):
#         return self.fullname  # прописать так для всех атрибутов
#
#     def set_birth_date(self, value):
#         self.birth_date = value
#
#     def set_tel(self, value):
#         self.tel = value
#
#     def set_city(self, value):
#         self.city = value
#
#
# human = Human(fullname='Stepa', birth_date='15.07.2002', tel='+79996780404', city='EKB', country='Russia')
# print(human.get_fullname())
# human.set_fullname('Marat')
# print(human.get_fullname())


# from typing import List
#
#
# class Student:
#
#     def __init__(self, fullname: str, group_num: str, mark_list: List):
#         self.fullname = fullname
#         self.group_num = group_num
#         self.marl_list = mark_list
#
#     def get_avg_mark(self) -> float:
#         return round(sum(self.marl_list) / len(self.marl_list), 1)
#
#     def __str__(self):
#         return f'{self.fullname} {self.group_num} {self.get_avg_mark()}'
#
#
# students = [
#     Student('Ivan', 'P-1', [2, 5, 4, 3, 4]),
#     Student('Marat', 'B-1', [2, 3, 4, 3, 1]),
#     Student('Stepa', 'D-1', [2, 5, 5, 3, 5]),
#     Student('Tema', 'R-1', [5, 5, 4, 4, 4]),
#     Student('Artem', 'T-1', [1, 1, 4, 3, 4]),
#     Student('Kolya', 'Y-1', [2, 5, 3, 3, 3]),
#     Student('Anton', 'U-1', [1, 5, 4, 5, 5]),
#     Student('Kaha', 'I-1', [4, 5, 5, 5, 4]),
#     Student('Markal', 'O-1', [1, 5, 1, 3, 1]),
#     Student('Roma', 'Q-1', [1, 5, 5, 5, 4])
# ]
#
# sorted_mark_students = sorted(students, key=lambda x: x.get_avg_mark())
# sorted_name_students = sorted(students, key=lambda x: x.fullname[0])
# sorted_group_students = sorted(students, key=lambda x: x.group_num[0])
#
# for i_stud in sorted_group_students:
#     print(i_stud)
