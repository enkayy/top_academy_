# string = 'Hello'
# encoded_string = string.encode(encoding='UTF-8')
# print(encoded_string)
# # b'Hello' -закодированная байт строка уже декодированная самим пайтоном
# decoded_string = encoded_string.decode(encoding='UTF-8')
# print(decoded_string) # раскодированная строка

# string = 'abcdefg'
# print(len(string))  # len - узнать длину строки
# print(string[0])  # получения символа из строки по индексу
# print(string[-1])  # последний элемент
# print(string[len(string) - 1])  # последний элемент
# print(string[0:3])  # срез
# print(string[:3])  # срез
# print(string[3:])  # срез
# print(string[0:5:2])  # 2 - шаг
# print(string[-1:3:-1])  # наооборот шаг -1
# print(string[::-1])  # Слово наоборот

# example = '0123456789'
# print(example[0:3])
# print(example[3:6])
# print(example[-1:-4:-1])
# print(example[0::2])
# print(example[::-1])
# print(example[5:2:-1])
# print(example[-2:3:-2])
# print(example[4:0:-1])

# text = 'python is a programming Language   '
# print(text.capitalize())  # первая буква большая, остальные маленькие
# print(text.title())  # каждое слово начинается с большой буквы
# print(text.count('p'))  # кол-во последовательностей в строке, можно считать одну букву, можно слова
# print(text.lower())  # вся строка в нижнем регистре
# print(text.upper())  # вся строка в верхнем регистре
# print(text.replace(' ', '-'))  # замена символа в строке
# print(text.index('n'))  # узнать индекс элемента, находит только первый, который встретил
# print(text.find('ж'))  # тоже самое, что и предыдущее, но вместо ошибки выводит -1
# print(text.index('Lang'))  # выводит начальный индекс
# print(len(text))
# print(len(text.rstrip()))  # убирает пробел справа просто strip - с обеих сторон lstrip - слева
# print(text.rfind('e'))  # начинает поиск справа, для ускорения
# print(text.swapcase())  # менять капс и строчные буквы

# Булевые функции

# string_2 = 'pythonruby'
# print(string_2.isalnum())  # проверят состоит ли строка только из букв или/и цифр
# print(string_2.isalpha())  # проверяет состоит ли строка только из букв
# print(string_2.isdigit())  # проверяет состоит ли строка только из цифр
# print(string_2.islower())  # проверка всей строки на нижний регистр
# print(string_2.isupper())  # проверка всей строки на верхний регистр
# print(string_2.isascii())  # есть ли эти символы в таблице ascii (Ё там нет)
# print(string_2.istitle())  # проверят начинается ли каждое слово с большой буквы
# print(string_2.isdecimal())  # проверка на целое число
# print(string_2.isnumeric())  # проверка на целое число
# print(string_2.isspace())  # проверка состоит ли строка только из пробелов
# string_2 = '+7999'
# print(string_2.startswith('+7'))  # проверяет первые симвоы в строке
# string_2 = 'test@mail.ru'
# # print(string_2.endswith('.ru'))  # проверяет последние символы
# print('@' in string_2)  # проверить есть ли символ в этой строке
# print(string_2.count('@') == 1)  # можно и так проверить на наличие символа

# string_3 = 'python ruby js'
# print(string_3.split('y'))  # делит строку по конкретному символ, по дефолту стоит пробел, можно поменять

# Задание 9

# string_9 = input('Введите текст: ')
# print(f'В вашем тексте {string_9.count("Ы")} больших букв Ы')
# print(f'В вашем тексте {string_9.count("ы")} маленьких букв Ы')


# # Email содержит (@, .ru .com)
# # Password содержит 8 символов, должен состоят из букв и цифр, без спецсимволов
# registration = False
#
# while not registration:
#     email = input('Введите email: ')
#     password_1 = input('Введите пароль: ')
#     password_2 = input('Подтвердите пароль: ')
#     if ('@' in email) and (email.endswith('.ru')) or (email.endswith('.com')):
#         if password_1 == password_2:
#             if (len(password_1) == 8) and (password_1.isalnum()) \
#             and not (password_1.isalpha()) and not (password_1.isdigit()):
#                 print('Вы зарегистрированы!')
#                 registration = True
#             else:
#                 print('Пароль должен быть длиной 8 символов, содежать цифры и буквы и не содержать спецсимволы')
#         else:
#             print('Пароли должны совпадать')
#     else:
#         print('Email должен содержать @ и заканчиваться на .ru или .com, попробуйте снова')


# # Регистрация по номеру телефона
#
# registration = False
#
# while not registration:
#     tel = input('Введите номер телефона в формате +79xxxxxxxxx: ')
#     if tel.startswith('+79') and len(tel) == 12 and tel[1].isdigit():
#         name = input('Введите ваше имя: ')
#         surname = input('Введите вашу фамилию: ')
#         if name.isalpha() and surname.isalpha():
#             print(f'\nВаше имя: {name.capitalize()}\n'
#                   f'Ваша фамилия: {surname.capitalize()}\n'
#                   f'Номер телефона: {tel}')
#             registration = True
#         else:
#             print('Невалидное имя или фамилия!')
#     else:
#         print('Невалидный номер телефона!')

# # Задание 1
#
# text = input('Введите текст: ')
# print(f'Ваш перевернутый текст: {text[::-1]}')


# # Задание 2
#
# text = input('Введите текст: ')
# count_num = 0
# count_alp = 0
# for i in text:
#     if i.isalpha():
#         count_alp += 1
#     elif i.isdigit():
#         count_num += 1
# print(f'Кол-во букв: {count_alp}\n'
#       f'Кол-во цифр: {count_num}')


# # Задание 3
#
# text = input('Введите текст: ')
# symbol = input('Введите символ для поиска: ')
# print(f'Кол-во сивмолов в строке: {text.count(symbol)}')


# # Задание 4
#
# text = input('Введите текст: ')
# word = input('Введите слово для поиска: ')
# print(f'Кол-во слов в строке: {text.count(word)}')


# # Задание 5
#
# text = input('Введите текст: ')
# word_find = input('Введите слово для поиска: ')
# word_change = input('Введите слово для замены: ')
#
# print(f'Ваша строка с замененным словом:\n'
#       f'{text.replace(word_find,word_change)}')


# # Задание 11
#
# st = input('Введите текст: ')
# subst = input('Введите строку для поиска в вашем тексте: ')
#
# if subst.lower() in st.lower():
#     print('Есть контакт!')
# else:
#     print('Мимо!')
