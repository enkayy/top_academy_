# --- Словари ---

# dictionary = {'name': 'Stepa', 'age': 21}

# print(dictionary)
# print(type(dictionary))

# name = dictionary.get('name')  # вызов по ключу
# age = dictionary.get('age')

# print(name)
# print(age)

# dictionary['age'] = 22  # Установка нового значения
# dictionary['surname'] = 'Padura'  # Можно добавить новые ключи и значения
# dictionary.pop('age')  # удаление по ключу
# dictionary.pop('asd')

# import sys
#
# list_man = ['Stepa', 21, 'Padura']
#
# print(sys.getsizeof(list_man))
# print(sys.getsizeof(dictionary))


# print(dictionary.keys())  # возвращает ключи словаря
# print(dictionary.values())  # возвращает значения словаря
# print(dictionary.items())  # возвращает все ключи и значения в виде кортежа

# dictionary_2 = {'name': 'Marat', 'age': 21}
# # Нельзя складывать словари
#
# dictionary.update(dictionary_2)  # обновляет значения первого словаря значениями другово словаря

#  item = dictionary.setdefault('age', '')  # устанавливает значение по умолчанию, если его изначально нет
# print(item)
#
# print(dictionary)

# # dictionary = {'Россия', [{'Ekb': {'population': 1233223}}, {}]}
#
# dictionary = {}
#
#
# def set_country(country):
#     dictionary.setdefault(country, [])
#     print('Страна добавлена!')
#
#
# def set_city():
#     key = input('Страна: ')
#     country = dictionary.get(key)
#     city_name = input('Введите название города: ')
#     if country or country == []:
#         for i_city in country:
#             if city_name in i_city.keys():
#                 print('Такой город уже есть!')
#                 return
#         population = int(input('Введите население города: '))
#         time_zone = input('Введите чаосвой пояс: ')
#         new_city = {city_name: {'population': population, 'time_zone': time_zone}}
#         dictionary[key].append(new_city)
#         print('Город добавлен!')
#     else:
#         print('Такой страны нет!')
#
#
# def get_city_info():
#     country = input('Введите страну: ')
#     get_country = dictionary.get(country)
#     if get_country:
#         city = input('Введите название города: ')
#         for i_city in get_country:
#             if city in i_city.keys():
#                 city_info = i_city[city]
#                 print(f'Население города: {city_info.get("population")}\n'
#                       f'Часовой пояс: {city_info.get("time_zone")}')
#                 return
#     else:
#         print('Такого страны нет!')
#
#
# def main():
#     while True:
#         choice = input('\n1 - Добавить страну\n'
#                        '2 - Добавить город\n'
#                        '3 - получить информацию по городу\n'
#                        '4 - Закончить программу -> ')
#         if choice == '1':
#             country = input('Введите название страны: ')
#             set_country(country)
#         elif choice == '2':
#             set_city()
#         elif choice == '3':
#             get_city_info()
#         elif choice == '4':
#             return
#
#
# main()


# Задача


# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         frequency_dict.setdefault(i_symbol, 0)
#         frequency_dict[i_symbol] += 1
#
# print(frequency_dict)
#
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

# # Без set_default
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         if i_symbol in frequency_dict.keys():
#             frequency_dict[i_symbol] += 1
#         else:
#             frequency_dict[i_symbol] = 1
#
# print(frequency_dict)


# for i_symbol in text:
#     if not i_symbol.isspace():
#         count = text.count(i_symbol)
#         if count in frequency_dict.keys():
#             if i_symbol not in frequency_dict[count]:
#                 frequency_dict[count].append(i_symbol)
#             else:
#                 frequency_dict[count] = [i_symbol]
#
#
# print(frequency_dict)

# # С setdefault
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         count = text.count(i_symbol)
#         frequency_dict.setdefault(count, [])
#         if i_symbol not in frequency_dict[count]:
#             frequency_dict[count].append(i_symbol)
#
# print(frequency_dict)


# # Для ДЗ
#
# dict_1 = {
#     'key1': {
#         'key2': {
#             'key3': 123,
#             'key4': {
#                 'key5': 'hello'
#             }
#         }
#     }
# }
#
# print(dict_1['key1']['key2']['key3'])
#
# dict_1['key1']['key2']['key3'] = 200
# print(dict_1)
