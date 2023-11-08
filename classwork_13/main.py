# --- Кортежи ---

# tuple_1 = (['Stepa'], 15)

# print(tuple_1[0])
# print(tuple_1[1])
# print(tuple_1[1:])

# tuple_2 = (tuple_1 + (['Petr'], 15))

# print(tuple_2 * 2)
# tuple_2[0][0] = 'Maria'  # Кортеж неизменяемый тип, но список внутри кортежа менять можно
# print(tuple_2)
# print(tuple_2.count(15))
# print(tuple_2.index(15))

# import sys
#
# tuple_1 = ('Stepan', 20)  # O(n)
# list_1 = ['Stepan', 20]  # O(n)
# dict_1 = {'Stepan': 20}  # O(1)
#
# print(sys.getsizeof(tuple_1))
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(dict_1))

# dict_1 = {('Stepa', 'Padura'): 25}  # В словаре можно хранить кортежи, но изменить его нелья
#
# print(dict_1['Stepa', 'Padura'])

# list_1 = ['Stepa', 'Padura']
# print(tuple(list_1))
#
# tuple_1 = ('Stepa', 'Padura')
# print(list(tuple_1))  # Можно преобразовать в список и обратно

# a = 10, 20  # Кортеж можно создать и так
# print(a)

# zip
#
# list_1 = ['Ekb', 'Msc', 'Spb']
# list_2 = (2000, 5000, 3000)
#
# print(dict(zip(list_1, list_2)))  # Если есть лишние значения, то он их отбросит list_2 = [2000, 5000, 3000, 12312]
# print(tuple(zip(list_1, list_2)))  # Получается кортеж с вложенными кортежами
# print(list(zip(list_1, list_2)))  # Получается список с вложенными кортежами

# import re
#
# dictionary = {}
#
#
# def add_competition() -> None:
#     competition = input('Введите название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) not in dictionary.keys():
#         dictionary.update({(competition, date): []})
#         print('Соревнование добавлено!')
#         return
#     print('Невалидный ввод')
#
#
# def add_member() -> None:
#     competition = input('Введите название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     # Можно вынести в отдельную функцию, потому что проверка повторяется
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         choice = input('Добавить/убрать участников соревнования add/del: ')
#         members = dictionary[(competition, date)]
#         if choice == 'add':
#             input_member = input('Введите участников через запятую: ').split(', ')
#             dictionary[(competition, date)] = members + input_member
#             print('Участники добавлены!')
#             return
#         elif choice == 'del':
#             del_members = input('Введите участников через запятую: ').split(', ')
#             for i_member in del_members:
#                 members.remove(i_member)
#             dictionary[competition, date] = members
#             print('Участники удалены')
#             return
#         else:
#             print('Невалидный ввод')
#
#
# def info() -> None:
#     competition = input('Введите название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     # Можно вынести в отдельную функцию, потому что проверка повторяется
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         print(f'{competition} {date}')
#         for index, i_member in enumerate(dictionary[competition, date]):  # разбивает значения на индекс и значение
#             print(f'{index + 1} {i_member}')
#         return
#     print('Такого соревнования нет!')
#
#
# def main() -> None:
#     while True:
#         choice = input('\n1 - Добавить соревнование\n'
#                        '2 - Внести участников соревнования\n'
#                        '3 - Вывод данных по конкретному соревнованию: ')
#         if choice == '1':
#             add_competition()
#         elif choice == '2':
#             add_member()
#         elif choice == '3':
#             info()
#
#
# main()

# Шифр цезаря
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# text = input('Введите текст для шифровки: ')
# shift = int(input('Введите сдвиг: '))
#
# print(caesar_code(text, shift))

# site = {
#     'body': {
#         'div': {
#             'ul': {
#                 'li_1': {},
#                 'li_2': {
#                     'a': {
#                         'href': 'ссылка'
#                     }
#                 }
#             }
#         }
#     }
# }
#
#
# def get(key, dictionary, level=0):
#     if key in dictionary.keys():
#         print(dictionary[key])
#         print(level)
#         return
#     for value in dictionary.keys():
#         if isinstance(dictionary[value], dict):  # если значения являются словарем
#             get(key, dictionary[value], level + 1)
#
#
# print(get('href', site))


# fruit_tuple = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
# fruit = input('Введите название фрукта: ')
# count = 0
#
# for i_fruit in fruit_tuple:
#     if fruit in i_fruit:
#         count += 1
#
# print(count)
# print(fruit_tuple.count(fruit))































