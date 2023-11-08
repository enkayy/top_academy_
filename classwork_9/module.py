# if __name__ == '__main__':
#     print('Я module')


# def summa(a, b, c):
#     return a + b + c
#
#
# print(summa(10, 10, 11))


# def print(string):
#     return string
#
#
# print('Hello')

# value_1 = 10  # Глобальная переменная
#
#
# def my_function():  # эта функция называется процедура, потому что она ничего не возвращает
#     global value_1  # можно вызвать внутри функции и изменять глобальную переменную
#     value_1 = 0
#     print(value_1)
#
#
# my_function()
# print(value_1)


# val_1 = 1
#
#
# def func_1(a=1):  # значение параметра по умолчанию
#     val_2 = 2
#
#     def func_2():  # замыкающая функция
#         nonlocal val_2  # ищет значение в верхней фуyкции, но не в глобально, для глобальной используем global
#         val_3 = 3
#         print(a)
#     print(val_2)
#     func_2()
#
#
# print(val_1)
# func_1()


# val_1 = 1.
#
#
# def func_1():
#     val_2 = 2
#
#     def func_2():
#         nonlocal val_2
#         val_2 += 3
#         if val_2 > 9:
#             return
#         print(val_2)
#         func_2()  # Рекурсия, которую можно прервать условием
#     print(globals())
#     print(locals())
#     print(val_2)
#     func_2()
#
#
# print(val_1)
# func_1()


# from math import *
#
# print(globals())

# import math
#
# print(globals())

# # Задание 7
#
#
# def check_is_happy_num(number: str) -> bool:  # принято прописывать тип данных, которые принимает и возврашает
#     """
#     Проверяет является ли число счастливым
#     :param number: str
#     :return: bool
#     """
#     left: int = int(number[0]) + int(number[1]) + int(number[2])
#     right: int = int(number[3]) + int(number[4]) + int(number[5])
#     if left == right:
#         return True
#     return False
#
#
# print(check_is_happy_num('123420'))


# # Задание от Никиты
#
# from typing import List
#
#
# def average_age(people: List[list]) -> float:  # List[int] List[float] List[str] List[any]
#     """
#     Функция среднего возраста
#     :param people: List[list]
#     :return: float
#     """
#     average: int = sum([i_human[1] for i_human in people])  # генератор
#     return round(average / len(people), 2)
#
#
# people_list = [
#     ['Ivan', 55],
#     ['Stepan', 10],
#     ['Marat', 20],
#     ['Anton', 32]
# ]
# print(average_age(people_list))


# # Задание 2
#
# from typing import List
#
#
# def odd_numbers_in_range(number_1: int, number_2: int) -> List[int]:
#     """
#     Функция, которая выводит нечетные числа
#     :param number_1: int
#     :param number_2: int
#     :return: List[int]
#     """
#     odd_num_list = []
#     for i_odd in range(number_1, number_2 + 1):
#         if i_odd % 2 != 0:
#             odd_num_list.append(i_odd)
#     return odd_num_list
#
#
# print(odd_numbers_in_range(1, 10))


# # Задание 3
#
#
# def drawing_line(length: int, direction: str, symbol: str) -> str:
#     """
#     Рисует линию из символов
#     :param length: int
#     :param direction: str
#     :param symbol: str
#     :return: str
#     """
#     if direction == 'hor':
#         for _ in range(length):
#             print(symbol, end='')
#     elif direction == 'vert':
#         for _ in range(length):
#             print(symbol)
#
#
# drawing_line(5, 'vert', '*')
# drawing_line(5, 'hor', '*')


# Задание 4

from typing import List


def simple_numbers(start: int, end: int) -> List[int]:
    """
    Ищет простые числа в диапазоне
    :param start: int
    :param end: int
    :return: List[int]
    """
    simple_num_list = []
    for i_simple in range(start, end + 1):
        for i in range(2, i_simple):
            if i_simple % i_simple == 0 and i_simple % i != 0:
                simple_num_list.append(i_simple)
    return simple_num_list


simple_numbers(1, 20)

# for i_simple_2 in range(i_simple):
#     if i_simple % i_simple_2 != 0 and i_simple % i_simple == 0:
#         simple_num_list.append(i_simple)
