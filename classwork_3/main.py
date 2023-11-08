# # Задача от Никиты 1
#
# time = int(input('Введите текущее время в часах: '))
#
# if 7 <= time <= 10:
#     print('Пора вставать!')
# elif time < 0 or time > 23:
#     print('Ошибка')
# else:
#     print('Ты проспал!')

# # Задача от Никиты 2
#
# exam_1 = int(input('Введите баллы за первый экзамен: '))
# exam_2 = int(input('Введите баллы за второй экзамен: '))
# exam_3 = int(input('Введите баллы за третий экзамен: '))
#
# summ = exam_1 + exam_2 + exam_3
#
# if summ >= 250:
#     print('Вы прошли на бюджет!')
# else:
#     print('У вас не хватает баллов на бюджет')

# # Задача от Никиты 3
#
# minutes = int(input('Введите кол-во минут: '))
# hours = minutes // 60
# minutes_left = minutes % 60
# print(f'{minutes} минут это {hours} часов и {minutes_left} минут')


# ЦИКЛЫ

# import time
#
# # лучше указывать i_..., i_num, потому что используем в цикле
# # если не используем переменную в самом цикле, то пишем _
# for _ in range(10):
#     # чтобы сделать задержку
#     # time.sleep(1)
#     print('Privet')

# for i in 'PADURA':
#     print(i + '*', end='')

# for i in range(0, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print('ok')

# for i in range(0, 5):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print('ok')

# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диаппазона: '))
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(f'{i} является нечетным')

# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диаппазона: '))
#
# for i in range(end, start - 1, -1):
#     print(i)

# summa = 0
# for i in range(1, 10000):
#     summa += i
# print(f'Сумма ряда равна: {summa}')

# number = int(input('Введите число: '))
# factorial = 1
#
# for i in range(2, number + 1):
#     factorial *= i
# print(f'Факториал числа {number} равен: {factorial}')

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print()

# correct_pin = 1547
#
# for i in range(3):
#     pin = int(input('Введите пин-код: '))
#     if pin == correct_pin:
#         print('Ваш пин-код верный!')
#         break
#     else:
#         print(f'Вы ввели неверный пин-код! Осталось попыток: {3 - (i + 1)}')
# else:
#     print('Вы 3 раза ввели неверный пин-код. Ваша карта заблокирована!')

# # Задача 1
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диаппазона: '))
#
# summa = 0
# count = 0
# for i in range(start, end + 1):
#     summa += i
#     count += 1
# print(f'Сумма ряда равна: {summa}')
# print(f'Средне арифметическое: {summa / count}')

# # Задача 3
#
# length = int(input('Введите длину линии: '))
#
# for _ in range(length):
#     print('*', end='')

# # Задача 4
#
# length = int(input('Введите длину линии: '))
# symbol = input('Введите символ: ')
#
# for _ in range(length):
#     print(symbol, end='')

# # Задача 1
#
# number = int(input('Введите число: '))
# mult = 0
#
# for i in range(1, 10):
#     mult = i * number
#     print(f'{number} * {i} = {mult}')

# # Задача 3
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диаппазона: '))
# number = int(input('Введите число: '))
#
# while number not in range(start, end + 1):
#     print('Число не входит в диапазон, попробуйте снова')
#     number = int(input('Введите число: '))
#
# print('Число входит в диапазон')
# for i in range(start, end + 1):
#     if i == number:
#         print(f'!{number}!', end=' ')
#         continue
#     print(i, end=' ')





