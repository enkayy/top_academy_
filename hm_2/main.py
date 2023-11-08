# # Задание 1
#
# try:
#     number1 = int(input('Введите первой число: '))
#     number2 = int(input('Введите второе число: '))
#     number3 = int(input('Введите третье число: '))
#
#     choice = int(input('Выберите операцию:\n1 - Сложение\n2 - Умножение\n'))
#     if choice == 1:
#         print(f'Резултат сложения: {number1 + number2 + number3}')
#     elif choice == 2:
#         print(f'Результат умножения: {number1 * number2 * number3}')
#     else:
#         print('Что-то пошло не так попробуйте снова')
# except ValueError:
#     print('\nНужно ввести число')


# # Задание 2
#
# try:
#     number1 = int(input('Введите первой число: '))
#     number2 = int(input('Введите второе число: '))
#     number3 = int(input('Введите третье число: '))
#
#     choice = int(input('\nВыберите операцию:\n1 - Максимум из 3 чисел'
#                        '\n2 - Минимум из 3 чисел\n3 - Среднеарифметическое\n'))
#
#     if choice == 1:
#         print(f'\nМаксимальное из чисел: {max(number1, number2, number3)}')
#     elif choice == 2:
#         print(f'\nМинимальное из чисел: {min(number1, number2, number3)}')
#     elif choice == 3:
#         print(f'\nСреднеарифметическое: {(number1 + number2 + number3) / 3}')
#     else:
#         print('\nЧто-то пошло не так попробуйте снова')
# except ValueError:
#     print('\nНужно ввести число')


# # Задание 3
#
# try:
#     meters = int(input('Введите количество метров: '))
#
#     choice = int(input('\nВыберите перевод метров в:\n1 - Мили'
#                        '\n2 - Дюймы\n3 - Ярды\n'))
#
#     if choice == 1:
#         print(f'\n{meters} метров = {meters * 0.000621371} миль')
#     elif choice == 2:
#         print(f'\n{meters} метров = {meters * 39.37} дюймов')
#     elif choice == 3:
#         print(f'\n{meters} метров = {meters * 1.094} ярдов')
#     else:
#         print('\nЧто-то пошло не так попробуйте снова')
# except ValueError:
#     print('\nНужно ввести число')
