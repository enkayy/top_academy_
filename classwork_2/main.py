# age = int(input('Введите ваш возраст: '))
# if 70 >= age >= 18:
#     print('Вы можете зарегистрироваться')
# else:
#     print('Вам нельзя зарегистрироваться')


# weekday = int(input('Введите номер дня недели: '))
#
# if weekday == 1:
#     print('Понедельник')
# elif weekday == 2:
#     print('Вторник')
# elif weekday == 3:
#     print('Среда')
# elif weekday == 4:
#     print('Четверг')
# elif weekday == 5:
#     print('Пятница')
# elif weekday == 6:
#     print('Суббота')
# elif weekday == 7:
#     print('Воскресенье')
# else:
#     print('Такого номера дня недели нет, попробуйте снова')

# email = 'padura@mail.ru'
# password = 'dikayasuka'
#
# email_input = input('Введите свой email: ')
# password_input = input('Введите пароль: ')
# authorization = False  # флаг, чтобы выводилась авторизация
#
# if email_input == email:
#     if password_input == password:
#         authorization = True
#         print('Вы авторизовались')
#     else:
#         print('Неправильный пароль')
# else:
#     print('Почта неправильная')
#
#
# # До версии 3.10 не работает, значит не нужно
# match(authorization):
#     case True:
#         print('Пользователь успешно авторизовался')
#     case False:
#         print('Пользователь не авторизовались')
# # аналог else но это не нужно
#     case _:
#         print('Else')

# number = int(input('Введите число: '))
#
# if number % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# number = int(input('Введите число: '))
#
# if number % 2 != 0:
#     print('Число нечетное')
# else:
#     print('Число четное')

# number = int(input('Введите число: '))
#
# if number % 6 == 0:
#     print('Число кратно 6')
# else:
#     print('Число не кратно 6')

# программа для решения квадратного уравнения
#
# можно подключить библиотеку и добавить корень sqrt
# если не будем импортировать math, то нужно будет прописывать math.sqrt
# from math import sqrt
# a = float(input('Введите коэф a: '))
# b = float(input('Введите коэф b: '))
# c = float(input('Введите коэф c: '))
#
# D = b**2 - 4 * a * c
# if D < 0:
#     print('Корней нет')
# elif D == 0:
#     x = -b / (2 * a)
#     print(f'\nx = {round(x, 2)}')
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - D ** 0.5) / (2 * a)
#     print(f'\nx1 = {round(x1, 2)}\nx2 = {round(x2, 2)}')

# number_1 = int(input('1-ое число: '))
# number_2 = int(input('2-ое число: '))
#
# try:
#     print(number_1 / number_2)
# # except BaseException: если не знаешь какая ошибка
# except ZeroDivisionError:
#     print('На ноль делить нельзя!!')
# else:
#     print('Программа выполнена без ошибок')
# finally:
#     print('Запускаем блок finally')
#
# if number_2 == 0:
#     print('На ноль делить нельзя!!')
# else:
#     print(number_1 / number_2)

# try:
#     raise ValueError('Вызвана ошибка специально')
# except FileNotFoundError:
#     print('Обработана ошибка')

# try:
#     raise ValueError
# except KeyError:
#     print('Обработчик ошибки ValueError 1')
# except ValueError:
#     print('Обработчик ошибки ValueError 2')

# try:
#     year = int(input('Введите год: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('Год високосный')
#     else:
#         print('Год не високосный')
# except (ValueError, TypeError):
#     print('Год должен быть числом!')

# Задача 2
#
# try:
#     number = int(input('Введите число: '))
#     if number % 7 == 0:
#         print(f'{number} Number is multiple 7')
#     else:
#         print(f'{number} Number is not multiple 7')
# except ValueError:
#     print('Нужно ввести число')

# Задача 3
#
# try:
#     number_1 = int(input('1-ое число: '))
#     number_2 = int(input('2-ое число: '))
#     if number_1 > number_2:
#         print(f'Первое число: {number_1} больше')
#     elif number_1 == number_2:
#         print(f'Числа {number_1} и {number_2} равны')
#     else:
#         print(f'Второе число: {number_2} больше')
# except ValueError:
#     print('Нужно ввести число')

# Задача 4
#
# try:
#     number_1 = int(input('1-ое число: '))
#     number_2 = int(input('2-ое число: '))
#     if number_1 < number_2:
#         print(f'Первое число меньше: {number_1}, {number_2}')
#     elif number_1 == number_2:
#         print(f'Числа {number_1} и {number_2} равны')
#     else:
#         print(f'Второе число меньше: {number_2}, {number_1}')
# except ValueError:
#     print('Нужно ввести число')

# Задача 5
#
# try:
#     number_1 = int(input('1-ое число: '))
#     number_2 = int(input('2-ое число: '))
#     choice = int(input('\nВыберите операцию: \n1 - сумма двух чисел \n2 - разница двух чисел \n3 - среднеарифметическое \n4 - произведение): '))
#     if choice == 1:
#         summ = number_1 + number_2
#         print(f'\nСумма двух чисел: {summ}')
#     elif choice == 2:
#         choice_diff = int(input('\nВычитаем первое из второго (напишите 1) или второе из первого (напишите 2): '))
#         if choice_diff == 1:
#             difference = number_1 - number_2
#             print(f'\nРазночть первого и второго числа: {difference}')
#         else:
#             difference = number_2 - number_1
#             print(f'\nРазность второго числа и первого: {difference}')
#     elif choice == 3:
#         print(f'\nСреднее арефмитическое двух чисел: {float(number_1 + number_2) / 2}')
#
#     elif choice == 4:
#         print(f'\nПроизведение двух чисел: {number_1 * number_2}')
# except ValueError:
#     print('Нужно ввести число')

try:
    time = int(input('Введите количество секунд от начала дня: '))
    choice = int(input('Выберите в чем вывести ответ: \n1 - секундах \n2 - минутах \n3 - часах\n'))
    if choice == 1:
        print(f'До конца дня осталось {43200 - time} секунд')
    elif choice == 2:
        print(f'До конца дня осталось {round(1800 - time / 60, 2)} минут')
    elif choice == 3:
        print(f'До конца дня осталось {round(12 - time / 1440, 2)} часов')
    else:
        print('Попробуйте снова')
except ValueError:
    print('Нужно ввести число')



