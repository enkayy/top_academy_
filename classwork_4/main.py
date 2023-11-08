# count = 0
#
# while count <= 5:
#     count += 1
#     print(count)


# # while True - бесконечный цикл, можно использовать, но нужно прервать
#
# count = 0
#
# while True:
#     count += 1
#     print(count)
#     if count == 5:
#         break


# number = int(input('Введите число: '))
#
# factorial = 1
#
# while number >= 1:
#     factorial *= number
#     number -= 1
#
# print(factorial)


# summa = 0
#
# while True:
#     number = float(input('Введите число или 0, чтобы закончить цикл: '))
#     if number == 0:
#         print(summa)
#         break
#     summa += number
# # print(summa) можно тут


# debt = 1000
# tries = 3
#
# while debt > 0:
#     money = int(input(f'Ваш долг составляет {round(debt, 2)}, сколько Вы готовы внести: '))
#     if money <= 0:
#         print('Сумма не может быть меньше или равной нулю')
#         continue
#     if tries > 0:
#         debt -= money
#     else:
#         print(f'Теперь начисляются проценты.')
#         debt *= 1.1
#         debt -= money
#     tries -= 1
# print('Вы закрыли долг')


# import random
#
# flag = True
#
# print('Программа на проверку заний таблицы умножения')
# level = int(input('1 - легкий\n2 - сложный\nВыберите уровень сложности: '))
#
# while flag:
#     if level == 1:
#         number_1 = random.randint(1, 9)
#         number_2 = random.randint(1, 9)
#     else:
#         number_1 = random.randint(10, 19)
#         number_2 = random.randint(10, 19)
#
#     result = number_1 * number_2
#     answer = int(input(f'{number_1} * {number_2} = '))
#     # if answer == result:
#     #     print('Правильный ответ!\t')
#     # else:
#     while answer != result:
#         print('Ответ неверный, попробуйте еще раз')
#         answer = int(input(f'{number_1} * {number_2} = '))
#     else:
#         print('Правильный ответ!\n')
#
#     choice = input('Продолжаем? Да/Нет -> ')
#     if choice == 'Нет':
#         print('Завершаю программу...')
#         flag = False


# import random
#
#
# guess_number = random.randint(1, 100)
# guessed = False
# count = 7
#
# while not guessed:
#     if count == 0:
#         print('У вас закончились попытки')
#         break
#     else:
#         print(f'Количество попыток: {count} ')
#         count -= 1
#
#     answer = int(input('Угадайте число от 1 до 100: '))
#     if answer == guess_number:
#         print('Вы угадали!')
#         guessed = True
#     elif answer > guess_number:
#         print('меньше\n')
#     elif answer < guess_number:
#         print('больше\n')


# # Задание 1
#
# number_1 = int(input('Введите x: '))
# number_2 = int(input('Введите y: '))
# result = 1
#
# while number_2 > 0:
#     result *= number_1
#     number_2 -= 1
#
# print(f'Ответ: {result}')


# # Задание 2
#
# count = 0
#
# for i in range(100, 1000):
#     hundred = i // 100
#     ten = (i % 100) // 10
#     one = i % 10
#
#     if hundred == ten or hundred == one or ten == one:
#         count += 1
#
# print(count)

# # Задание 3
#
# count = 0
#
# for i in range(100, 999):
#
#     hundred = i // 100
#     ten = (i % 100) // 10
#     one = i % 10
#
#     if hundred == ten or hundred == one or ten == one:
#         count += 1
#
# for i in range(1000, 10000):
#     thousand = i // 1000
#     hundred = i % 1000 // 100
#     ten = i % 100 // 10
#     one = i % 10
#
#     if hundred == ten or hundred == one or ten == one or thousand == hundred or thousand == ten or thousand == one:
#         count += 1
#     i += 1
# result = 9889 - count
# print(result)






