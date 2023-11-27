# print('Hello world!')

# sep = '' всегда в кавычка по дефолту пробел, рвзделитель между словами
# \t -> табуляция
# \n -> переход на новую строку
print("Hello,", "Stepan", "!", sep="\t")

# end -> что стоит в конце строки, по дефолту \n, применяется к одной строке
# print('Hello Python!', end=' ')
# print('Hello Ruby!', end=' ')
# print('Hello Java!')

# number_1 = 50  # Snake case -> формат обозначения в python
# number_2 = 75

# print(number_1 + number_2)
# print(number_1 * number_2)
# print(number_1 / number_2)
# print(number_2 // number_1)  # целочисленное деление
# print(number_2 % number_1)  # остаток от деления

# value_1 = '41'
# value_2 = '56'
# Конкатенация
# print(value_1 + value_2)

# value_1 = 41  # Garbage collector
# value_2 = 56
#
# value_1 = 10
# print(value_1)

# number = int(5.6)
# float_number = float(5)
# print(number)
# print(float_number)
# # e+6 -> число умноженное на 10 в какой-то степени
# print(8e+6)
# # type определяет тип данных переменной
# print(type(str(45)))

# Логический тип (Boolean)-> bool()

# print(bool(1))
# print(bool(0))  # False
# print(bool(-2))
# print(bool(''))  # False
# print(bool('dsfsdf'))

# print(2 == 2)
# print(1.1 + 2.2)
# print(1.1 + 2.2 == 3.3)
# print(round(1.1 + 2.2, 1) == 3.3)
# print(15 > 12)
# print(15 < 12)
# print(15 >= 22)
# print(15 <= 22)
# print(15 != 22)  # неравно
# print('d' > 'B')

# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# # # print('Привет, ' + name + '!' + ' Вам уже ' + str(age) + ' лет') неудобно
# # # Форматирование строк
# # старый метод, которым уже почти не пользуются
# # print('Привет, {val_1}! Вам уже {val_2} лет'.format(val_1=name, val_2=age))
# # print('Привет, {0}! Вам уже {1} лет'.format(name, age))  # можно по номерам страницы, но это тоже самое
# print(f'Привет, {name}! Тебе уже {age} лет')

# number = int(input('Введите трехзначное число: '))
# first_num = number // 100
# second_num = number // 10 % 10
# third_num = number % 10
# print(f'{first_num}\n{second_num}\n{third_num}\n{first_num + second_num + third_num}')

# import time
#
# print(time.time() / 3600 / 24 / 365)

# Задача 3
# number_1 = input('Введите цифру: ')
# number_2 = input('введите цифру: ')
# print(number_1 + number_2)

# Задача 4
# celcius = int(input('Введите температуру в целсиях: '))
# print(f'Перевод из градусов цельсия в градусы фаренгейта: {1.8 * celcius + 32}')

# Задача от Никиты
# number = int(input('Введите четырехзначное число: '))
# num_1 = number // 1000
# print(num_1)
# num_2 = number // 100 % 10
# print(num_2)
# num_3 = number // 10 % 10
# print(num_3)
# num_4 = number % 10
# print(num_4)
# print(num_1 * num_2 * num_3 * num_4)
# print(str(num_4) + str(num_3) + str(num_2) + str(num_1))

# Крутая задача от Никиты
# number = int(input('Введите число от 1 до 100: '))
# if 100 > number < 1:
#     print('Вы ввели неправильное число')
# elif number % 3 == 0 and number % 5 == 0:
#     print('Fizz Buzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)
