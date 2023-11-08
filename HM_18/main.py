# # Задание 1
#
#
# class Automobile:
#
#     def __init__(self, brand: str, model_name: str, release_year: int, engine_capacity: float, color: str, cost: int):
#         self.model_name = model_name
#         self.release_year = release_year
#         self.brand = brand
#         self.engine_capacity = engine_capacity
#         self.color = color
#         self.cost = cost
#
#     def get_engine_capacity(self):
#         return f'Объем двигателя {self.brand} {self.model_name}: {self.engine_capacity} л.'
#
#     def get_year_and_cost(self):
#         return f'Машина {self.release_year} г. {self.brand} {self.model_name} {self.color.lower()} цвет'
#
#     def __str__(self):
#         return f'\nАвтомобиль: {self.brand} {self.model_name}\n' \
#                f'\tГод выпуска: {self.release_year}\n' \
#                f'\tОбъем двигателя: {self.engine_capacity}\n' \
#                f'\tЦвет: {self.color}\n' \
#                f'\tСтоимость: {self.cost}\n'
#
#
# automobile_1 = Automobile('Audi', 'A5', 2013, 2.0, 'Белый', 1250000)
# print(automobile_1)
# print(automobile_1.get_engine_capacity())
# print(automobile_1.get_year_and_cost())


# # Доп задание
#
# from random import randint as rnd
#
#
# class Duel:
#
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.damage = 20
#
#     def hit(self, warrior):
#         warrior.health -= self.damage
#         if warrior.health > 0:
#             print(f'{self.name} атаковал {warrior.name}. У {warrior.name} осталось {warrior.health} здоровья')
#         else:
#             print(f'{self.name} атаковал {warrior.name}. {warrior.name} убит')
#             warrior.health = 0
#         return warrior.health
#
#     def __str__(self):
#         return f'{self.name}, {self.health} здоровья.'
#
#
# warriors = [Duel('Воин 1'), Duel('Воин 2')]
#
# while True:
#     attacker = rnd(0, 1)
#     target = (attacker + 1) % 2
#     target_health = warriors[attacker].hit(warriors[target])
#     if target_health == 0:
#         print(f'{warriors[attacker].name} победил!')
#         break




















