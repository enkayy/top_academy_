
# Задание 1

from typing import Callable
import random


def random_error(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        errors_list = [ZeroDivisionError, TypeError, ValueError, SyntaxError, OverflowError]
        if random.randint(1, 10) == 1:
            raise Exception(random.choice(errors_list))
        return func(*args, *kwargs)
    return wrapper


# Задание 2


# def data_type(func: Callable) -> Callable: # тут просто выводится тип данных, который вернула функция
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(type(res))
#         return res
#     return wrapper

def data_type(func: Callable) -> Callable:
    # тут идет проверка, но я не понял, что именно она должна делать, поэтому
    # вызываю ошибку, если тип данных не подходит
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            print('Функция вернула строку')
        elif isinstance(res, int):
            print('Функция вернула число (int)')
        else:
            raise Exception('Функция вернула не str и int')
            # print('Функция вернула не str и int')
        return res
    return wrapper


@data_type
@random_error
def division(a, b):
    """
    Деление двух чисел
    :param a: int
    :param b: int
    :return: float
    """
    return (a / b)
    # return 'sadasd'


print(division(10, 2))
