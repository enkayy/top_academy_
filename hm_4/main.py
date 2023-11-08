# # Задание 1
#
# start = int(input('Ведите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
#
# num_7 = []
#
# print('Числа кратные 7: ', end='')
# for i in range(start, end + 1):
#     if i % 7 == 0:
#         print(i, end=' ')

# # Задание 2
#
# start = int(input('Ведите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# count_5 = 0
# num_list = []
#
# print('Все числа диапазона: ', end='')
# for i_num in range(start, end + 1):
#     print(i_num, end=' ')
# print('')
#
# print('Все числа диапазона в обратном порядке: ', end='')
# for i_mun in range(end, start - 1, -1):
#     print(i_mun, end=' ')
# print('')
#
# print('Все числа диапазона кратные 7: ', end='')
# for i in range(start, end + 1):
#     if i % 7 == 0:
#         print(i, end=' ')
#     if i % 5 == 0:
#         count_5 += 1
# print('')
# print(f'Количество чисел кратных 7: {count_5}')

# # Задание 3
#
# start = int(input('Ведите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
#
# for i in range(start, end + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz.')
#     elif i % 3 == 0:
#         print('Fizz.')
#     elif i % 5 == 0:
#         print('Buzz.')
#     else:
#         print(i)
