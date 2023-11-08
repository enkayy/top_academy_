
# # Задание 1
#
#
# def multiply(*args: int) -> int:
#     """
#     Умножает переданные занчения
#     :param args: int
#     :return: int
#     """
#     product = 1
#     for i_num in args:
#         product *= i_num
#     return product
#
#
# print(multiply(1, 2, 3, 4))


# # Задание 2
#
#
# def minimum(*args: int) -> int:
#     """
#     Находит минимальное значение
#     :param args: int
#     :return: int
#     """
#     return(min(args))
#
#
# print(minimum(23, 43, 110))


# # Задание 3
#
# from typing import List
#
#
# def simple_num(*args: int) -> List:
#     """
#     Считает количество простых чисел
#     :param args: int
#     :return: List, int
#     """
#     simple_list = []
#     for i_num in args:
#         for i_del in range(2, i_num // 2):
#             if i_num % i_del == 0:
#                 break
#         else:
#             simple_list.append(i_num)
#     return simple_list
# # Неправильно прочитал и вывел список, если по заданию, то просто заменить список на счетчик,
# # вместо simple_list.append(i_num) написать count += 1 и вывести не список, а число
#
#
# print(simple_num(3, 7, 8, 13, 22))


# # Задание 4
#
# from typing import List
#
#
# def del_num(num: int, *args: int) -> List:
#     """
#     Удаляет число из списка
#     :param num: int
#     :param args: int
#     :return: List
#     """
#     num_list = list(args)
#     for i_num in args:
#         if i_num == num:
#             num_list.remove(num)
#     return num_list
#
#
# print(del_num(1, 23, 5, 1, 6, 1, 7, 1))


# # Задание 5 через списки
#
# from typing import List
#
#
# def list_combine(list_1: List, list_2: List) -> list:
#     """
#     Объеденение двух списков
#     :param list_1: List
#     :param list_2: List
#     :return: List
#     """
#     combined_list = list_1 + list_2
#     return combined_list
#
#
# print(list_combine([1, 2, 3, 4], [10, 9, 20, 11]))


# # Задание 6
#
#
# from typing import List
#
#
# def raise_to_power(power: int, *args: int) -> List:
#     """
#     Возводит в степень элементы списка
#     :param power: int
#     :param args: int
#     :return: List
#     """
#     raised_num_list = []
#     for i_num in args:
#         raised_num_list.append(i_num**power)
#     return raised_num_list
#
#
# print(raise_to_power(3, 2, 3, 4, 5, 6, 7, 8, 9, 10))

















