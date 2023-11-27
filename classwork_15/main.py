# --- Декораторы ---


# from typing import List
# import datetime
# from typing import Callable
# import time
#
#
# # def timer(func: Callable, *args, **kwargs):
# #     print('Запускается таймер...')
# #     start = time.time()
# #     res = func(*args, **kwargs)
# #     print(f'Функция {func.__name__} выполнялась {time.time() - start}')
# #     return res
#
# import functools
#
#
# def timer(func: Callable) -> Callable:
#     @functools.wraps(func)  # Раньше нужно было явно передать функцию обертку, чтобы не заменялся документал
#     def wrapper(*args, **kwargs):  # функция обертка, добавляем арги и кварги, если в функцию передаются параметры
#         start = time.time()  # код для дополнения функционала
#         func(*args, **kwargs)  # вызов функции, которую передали, сюда тоже нужно передать арги и кварги
#         print(f'Функция {func.__name__} {func.__doc__} выполнилась за {time.time() - start}')  # код для дополнения функционала
#     return wrapper  # всегда нужно вернуть функцию обертку
#
#
# @timer  # декоратор прописывается перед функцией
# def squares_sum(num: int) -> List:
#     """
#     Квадраты чисел
#     :param num: int
#     :return: List
#     """
#     nums = [i ** 2 for i in range(num)]
#     return nums
#
#
# @timer
# def cubes_sum():
#     """
#     Кубы чисел
#     :return: List
#     """
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
#
# squares_sum(1000000)
# cubes_sum()
#
# # res = timer(squares_sum, 1000000)
# # res_2 = timer(cubes_sum, 1000000)


# def get_or_post(method):  # если передаем параметр, то нужна еще одна ступенька для вызова функции
#     def wrapper_func(func):  # если передаем параметр, то нужна еще одна ступенька для вызова функции
#         def wrapper():
#             res = func()
#             print(f'Запрос с методом {method} на ресурс {res} выполнен')
#         return wrapper
#     return wrapper_func
#
#
# @get_or_post('POST')  # с помощью декоратора можно передавать параметр
# def request():
#     url = 'http://test.com'
#     params = 'ru'
#     request_body = {}
#     return url, params, request_body
#
#
# request()


# def beauty_output(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         count = 1
#         for i in res:
#             print(f'{count}. {i} <3')
#             count += 1
#     return wrapper
#
#
# @beauty_output
# def names_output(names):
#     # Что-то ту делаем с именами и возвращаем измененный вид
#     return names
#
#
# names_output(['Stepa', 'Marat', 'Tema'])

# import datetime
# import functools
#
#
# def logging(func: Callable) -> Callable:  # Записывает ошибку в log файл
#     @functools.wraps(func)  # делаем functools, потому что подменяет функцию на wrapper
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'{func.__name__} {func.__doc__}')
#         except BaseException as error:
#             with open('Functions_error.log', 'a') as file:
#                 file.write(f'{func.__name__} | {datetime.datetime.now()} | {error}\n')
#                 # error.__doc__ - подробное описание ошибки
#
#     return wrapper
#
#
# @timer  # можно применять несколько декораторов для одной функции
# @logging
# def concatenate(a, b):
#     """
#
#     :param a:
#     :param b:
#     :return:
#     """
#     return a + b
#
#
# @timer
# @logging
# def division(a, b):
#     """
#
#     :param a:
#     :param b:
#     :return:
#     """
#     return a / b
#
#
# concatenate(21, 1)
# division(21, 1)


# Задание
# написать декоратор, который вызывает функцию 2 раза

import time
from typing import Callable
from time import sleep


# def sleep_func(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper


# def double_func(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         res_2 = func(*args, **kwargs)
#         print(res)
#         print(res)
#     return wrapper


# def repeat_func(repeats):
#     def wrapper_func(func: Callable) -> Callable:
#         def wrapper(*args, **kwargs):
#             for i in range(repeats):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return wrapper_func


# def check_age(func: Callable):
#     def wrapper(*args, **kwargs):
#         age = int(input('Сколько вам лет? -> '))
#         if age >= 18:
#             print('Доступ разрешен!')
#             res = func(*args, **kwargs)
#             print(res)
#         else:
#             print('Вам еще нет 18 лет!')
#     return wrapper

# func_dict = {}
#
#
# def reg_func(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         func_dict.setdefault(func.__name__, func.__doc__)
#         return func_dict
#     return wrapper


# @sleep_func
# @repeat_func(3)
# @double_func
# @check_age
# @reg_func
# def division(a, b):
#     """
#     Деление двух чисел
#     :param a: int
#     :param b: int
#     :return: float
#     """
#     return a / b
#
#
# @reg_func
# def summ(a, b):
#     """
#     Сумма чисел
#     :param a: int
#     :param b: int
#     :return: int
#     """
#     return a + b
#
#
# print(division(10, 2))
# print(summ(2, 3))
#
# print(func_dict)


# num_list = []
#
#
# def simple_num(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         with open('simple_num.txt', 'a') as file:
#             for i_num in res:
#                 for i_del in range(2, i_num):
#                     if i_num % i_del == 0:
#                         break
#                 else:
#                     file.write(f'{i_num}\n')
#
#     return wrapper
#
#
# @simple_num
# def nums(a, b):
#     for i in range(a, b + 1):
#         num_list.append(i)
#     return num_list
#
#
# nums(1, 10)
