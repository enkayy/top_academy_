# --- Словари Повторяем ---

# # Учет прибыли
#
# import re
#
# data = {}
#
#
# def add_money() -> None:
#     date = input('yyyy/mm -> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, {})
#         data[year].setdefault(month, 0)
#         data[year][month] += money
#         sorted_data = dict(sorted(data[year].items()))
#         print(sorted_data)
#         # dict(sorted(data[year].items))
#         # print(data)
#     else:
#         print('Формат даты неверный!')
#
#
# def get_year_cost() -> None:
#     year = input('yyyy -> ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} составляет: {sum(data[year].values())}')
#     else:
#         print('Такого года нет')
#
#
# def get_month_cost() -> None:
#     date = input('yyyy/mm -> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         year, month = date.split('/')
#         if year in data.keys():
#             if month in data[year].keys():
#                 print(f'Ваша прибыль за {date} составила: {data[year][month]} KZT')
#             else:
#                 print('Такого месяца нет!')
#         else:
#             print('Такого года нет!')
#     else:
#         print('Неверный формат даты!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1 - Внести прибыль за период в формате yyyy/mm\n'
#                        '2 - Получить прибыл за конкретный месяц (yyyy/mm)\n'
#                        '3 - Получить прибыл за конкретный год (yyyy)\n'
#                        '4 - Выйти из программы -> ')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         elif choice == '4':
#             print('Завершение работы программы...')
#             break
#         else:
#             print('Такой команды нет!')
#
#
# main()

# # Вариант с другим методом хранения
#
# import re
#
# data = {}
#
#
# def add_money() -> None:
#     date = input('yyyy/mm -> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, 0)
#         data.setdefault(date, 0)
#         data[year] += money
#         data[date] += money
#         sorted_data = dict(sorted(data.items()))
#         print(sorted_data)
#     else:
#         print('Формат даты неверный!')
#
#
# def get_year_cost() -> None:
#     year = input('yyyy -> ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} составляет: {data[year]}')
#     else:
#         print('Такого года нет')
#
#
# def get_month_cost() -> None:
#     date = input('yyyy/mm -> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         if date in data.keys():
#             print(f'Ваша прибыль за {date} составила: {data[date]} KZT')
#         else:
#             print('Такого месяца нет!')
#     else:
#         print('Неверный формат даты!')
#
#
# def main() -> None:
#     while True:
#         choice = input('\n1 - Внести прибыль за период в формате yyyy/mm\n'
#                        '2 - Получить прибыл за конкретный месяц (yyyy/mm)\n'
#                        '3 - Получить прибыл за конкретный год (yyyy)\n'
#                        '4 - Выйти из программы -> ')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         elif choice == '4':
#             print('\nЗавершение работы программы...')
#             break
#         else:
#             print('Такой команды нет!')
#
#
# main()

import re

contacts = {}


def add_contact() -> None:
    tel = input('\nВведите номер телефона в формате 8xxxxxxxxxx: ')
    name = input('Введите имя контакта: ')
    if re.match(r'\d{11}', tel):
        contacts.setdefault(tel, name)
    else:
        print('Неверный формат номера телефона!')


# def add_contact() -> None:
#     tel = input('\nВведите номер телефона контакта, который вы хотите удалить,'
#                 'если телефонов несколько, то вводите через пробел: ')
#     name = input('Введите имя контакта: ')
#     tel_list = tel.split(' ')
#     for i_num in tel_list:
#         if re.match(r'\d{11}', i_num):
#             contacts.setdefault(tel_list, name)
#         else:
#             print('Неверный формат номера телефона!')


def del_contact() -> None:
    tel = input('\nВведите номер телефона контакта, который вы хотите удалить: ')
    if re.match(r'\d{11}', tel):
        if tel in contacts.keys():
            print(f'Контакт "{contacts[tel]}" с номером {contacts.get("", tel)} удален')
            del contacts[tel]
    else:
        print('Неверный формат номера телефона!')


def edit_contact() -> None:
    tel = input('\nВведите номер телефона контакта, который вы хотите отредактировать: ')
    print('Если вы не собираетесь редактировать имя или номер, поставте -')
    new_tel = input('Введите новый номер телефона: ')
    new_name = input('Введите новое имя контакта:')
    if new_name == '-':
        if re.match(r'\d{11}', tel) and re.match(r'\d{11}', new_tel):
            if tel in contacts.keys():
                name = contacts[tel]
                print(f'Номер телефона у контакта "{contacts[tel]}" измененн: '
                      f'\nСтарый номер - {contacts.get("", tel)}'
                      f'\nНовый номер - {new_tel} ')
                del contacts[tel]
                contacts.setdefault(new_tel, name)
        else:
            print('Неверный формат номера телефона!')

    elif new_tel == '-':
        if tel in contacts.keys():
            print(f'Номер телефона у контакта "{contacts[tel]}" измененно на {new_name}: ')
            contacts.update(tel)
        else:
            print('Такого номера телефона нет!')


def main():
    while True:
        choice = input('\n1 - Добавить контакт\n'
                       '2 - Удалить контакт\n'
                       '3 - Редактировать контакт\n'
                       '4 - Показать текущие контакты\n'
                       '5 - Завершить программу -> ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            del_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            print(f'\n{contacts}')
        elif choice == '5':
            print('\nЗавершение работы программы...')
            break
        else:
            print('\nТакой функции нет!')


main()


# Синтаксический сахар

# def info_man(name, age):  # Достает из словаря значения
#     print(name, age)
#
#
# data = {'name': 'Ivan', 'age': 22}
#
# info_man(**data)  # Распаковка словаря


# def info_man_2(name, age):  # Тоже, что и со словарем, но важно соблюдать порядок в списке, в словаре по ключам
#     print(name, age)
#
#
# list_info = ['Ivan', 22]
#
# info_man_2(*list_info)  # Распаковка списка

# name_list = ['Stepan', 'Ivan', 'Maria', 'Marat']
#
# names_dict = {i + 1: name_list[i] for i in range(len(name_list))}  # Генератор словарей,
# # тоже что и генератор списка, только с ключами
# names_dict_2 = {i: [i for i in range(10)] for i in name_list}
# names_dict_3 = {i: [j for j in i] for i in name_list}
#
# print(names_dict)
# print(names_dict_2)
# print(names_dict_3)
