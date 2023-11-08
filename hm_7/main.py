# # Задание 1
#
# operation = input('Введите арифметическую операцию: ')
#
# if '+' in operation:
#     result = [int(item) for item in operation.split('+')]
#     print(sum(result))
# elif '-' in operation:
#     a, b = operation.split('-')
#     print(int(a) - int(b))
# elif '*' in operation:
#     a, b = operation.split('*')
#     print(int(a) * int(b))
# elif '/' in operation:
#     a, b = operation.split('/')
#     print(int(a) / int(b))


# # Задание 2
#
# from random import randint
#
# rand_num_list = []
# count_negative = 0
# count_positive = 0
# count_zero = 0
#
# for _ in range(20):
#     rand_num_list.append(randint(-100, 100))
#
# for i in rand_num_list:
#     if i < 0:
#         count_negative += 1
#     elif i > 0:
#         count_positive += 1
#     elif i == 0:
#         count_zero += 1
#
# print(f'Случайный список из чисел: {rand_num_list}')
# print(f'Максимальный элемент: {max(rand_num_list)}')
# print(f'Минимальный элемент: {min(rand_num_list)}')
# print(f'Количество отрицательных элементов: {count_negative}')
# print(f'Количество положительных элементов: {count_positive}')
# print(f'Количество нулей: {count_zero}')
