# # Задание 1
#
# summ = 0
# number = 1
# while number != 0:
#     number = int(input('Введите число: '))
#     summ += number
# print(summ)

# # Задание 2
#
# password = '235'
# while True:
#     password_inp = input('Введите ваш пароль: ')
#     if password_inp == password:
#         print('Пароль верный! Добро пожаловать.')
#         break
#     else:
#         print('Неверный пароль!\n\nПопробуйте еще раз')

# # Задание 3
#
# summ = 500000
# cred_summ = 0
#
# while True:
#     cred = int(input('Сколько отложить денег? - > '))
#     cred_summ += cred
#
#     if cred_summ >= summ:
#         print(f'Вы накопили {cred_summ} рублей. Теперь на машину хватает')
#         break
#     else:
#         print(f'Вам осталось накопить еще {summ - cred_summ} рублей')

# # Задание 4
#
# pin = 1098398495324
# str_pin = str(pin)
# reversed_pin = (str_pin[::-1])
# summ = 0
#
# for num in reversed_pin:
#     if num != '5':
#         int_num = int(num)
#         summ += int_num
#     else:
#         break
# print(f'Сумма чисел: {summ}')

# # Задание 5
#
# import time
#
# count = 10
#
# while count != 0:
#     print(count)
#     count -= 1
#     time.sleep(1)
#
# print('Время вышло!')

# # Задание 6
#
# import time
#
# hour = int(input('Который час? - > '))
#
# while hour != 0:
#     print('Ку-ку!')
#     hour -= 1
#     time.sleep(0.5)

# # Задание 7
#
# import time
#
# sec = int(input('Сколько считать? - >  '))
#
# for i_sec in range(sec, 0, -1):
#     print(sec)
#     sec -= 1
#     time.sleep(1)
#
# print('Я иду искать!')

# # Задание 8
#
# text = input('Введите текст: ')
#
# print(f'Больших букв Ы: {text.count("Ы")}')
# print(f'Маленьких букв Ы: {text.count("ы")} ')

# # Задание 9
#
# text = input('Введите текст: ')
#
# print(text.title())

# # Задание 10
#
# import random
#
# summ = 0
#
# while summ < 666:
#     rand_num = random.randint(1, 13)
#     if rand_num != 13:
#         number = int(input('Введите число: '))
#         summ += number
#     else:
#         raise Exception('Вы проиграли :(')  # Не знаю, как вывести рандоиное исключение
#
#     if summ >= 666:
#         print('Вы выиграли!')

# # Задание 11
#
# text = 'sdfsdfwehsdfsdrwehsdfsdf'
#
# left_h = text.index('h')
# right_h = text.rindex('h') - 1
# reversed_text = text[right_h:left_h:-1]
#
# print(reversed_text)

# # Решение используя указатели
#
# text = 'sdfhqwertyhsdf'
#
# start = -1
# end = -1
#
# for i in range(len(text)):
#     if text[i] == 'h':
#         start = i
#         break
#
# for i in range(len(text) - 1, 0, -1):
#     if text[i] == 'h':
#         end = i
#         break
#
# print(text[end - 1:start:-1])
