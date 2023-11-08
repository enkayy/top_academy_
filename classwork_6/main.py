# import sys
#
# my_list_1 = ['Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg',]  # первый способ задать список.
# # Ставим запятую в конце, если список будет дополнятся
# # ['Moscow', ['Samara'], 'Saint-P', 'Vorcuta', 'Ekaterinburg',]
# # Можно делать список в списке, но хранить будет он только адреса внутреннего списка
#
# my_list_2 = list(('Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg'))  # второй способ вызвать список
# # Если вызывать с помощью list, то список будет меньше весить, потому что он хранит только адреса
#
# print(my_list_1)
# print(my_list_2)
# print(sys.getsizeof(my_list_1))
# print(sys.getsizeof(my_list_2))

# my_list_1 = ['Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg', ]
#
# print(my_list_1[0])
# print(my_list_1[1:])
# print(my_list_1[::2])
# print(my_list_1[::-1])

# my_list_1 = ['Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg', 'Ekaterinburg',]
#
# my_list_1.append('Chita')  # append добавляет элемент в конец списка
# my_list_1.append('Chita')
# my_list_1.remove('Chita')  # удаляет первое вхождение по значению, то есть удаляется один дубликат
# del_city = my_list_1.pop(0)  # удаляет элемент по индексу, по умолчанию стоит -1
# # также можно присвоить переменную и вывести удаленный элемент
# my_list_1.insert(0, 'Kazan')  # используется, чтобы поставить элемент на определенную позицию в списке по индексу
# # остальные элементы двигаются
# print(my_list_1.index('Ekaterinburg'))  # выводит индекс по значению переменной, возвращает первый найденный
# print(my_list_1.count('Ekaterinburg'))  # выводит количество конткретного эелемента списка
# print(my_list_1)
# print(del_city)

# my_list_1 = ['Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg', 'Ekaterinburg',]
#
# my_list_1[4] = 'Vladikvostok'  # можно заменить элемент в определенном индексе
# my_list_1.reverse()  # разворачивает список
#
# print(my_list_1)

# my_list_1 = ['Moscow', 'Samara', 'Saint-P', 'Vorcuta', 'Ekaterinburg', ]
#
# for i_city in my_list_1:
#     print(f'City: {i_city}')
#
# for index in range(len(my_list_1)):
#     print(f'{index + 1} City: {my_list_1[index]}')

# # Задание 1
#
# start = int(input('Введите начало диаппазона: '))
# end = int(input('Введите конец диаппазона: '))
# odd_list = []
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         odd_list.append(i)
#
# print(odd_list)

# # Задание 2
#
# basket_1 = ['Bayern', 'MU', 'Juventus', 'Arsenal']
# basket_2 = ['Barselona', 'Man City', 'Milan', 'Real Madrid']
#
# for index in range(len(basket_1)):
#     if index % 2 != 0:
#         print(f'{basket_1[index]} - {basket_2[index - 1]}')
#         print(f'{basket_1[index - 1]} - {basket_2[index]}')


# numbers = [15, 23, 55, 6, 98, 45, 2]
# numbers.sort(reverse=False)  # осортировать спискок. reverse=True - по убываниюю. Применяется к самому списку
# numbers_sorted = sorted(numbers)  # создает копию, поэтому нужно присвоит переменную, чтобы вывести
# print(id(numbers_sorted), id(numbers))
# print(numbers == numbers_sorted)

# letters = ['a', 'z', 't', 'b', 'r', 'Z']  # сортирует по значению в таблице юникод
# print(sorted(letters))

# string = 'hello*python*java*ruby'
# print(string.split('*'))


# numbers = input('Введите числа через пробел: ').split()
#
# for i_num in numbers:
    # numbers[numbers.index(i_num)] = int(i_num)  # переводит числа из строчного(string) варианта в числовой(int)
#
# for index, value in enumerate(numbers):  # нужно два значения для enumerate
#     numbers[index] = int(value)  # второй способ
#
# numbers_int = list(map(int, input('Введите числа через пробел: ').split()))  # третий способ самы короткий и правильный?
#
# print(numbers_int)


# films = ['Форсаж 1', 'Форсаж 2', 'Форсаж 3', 'Форсаж 4', 'Форсаж 5', 'Форсаж 6', 'Форсаж 7',
#          'Форсаж 8', 'Форсаж 9', 'Форсаж 10']
# liked_films = []
#
# while True:
#     choice = input('1 - Посмотреть список избранных фильмов\n'
#                    '2 - Добавить фильм в избранное\n'
#                    '3 - Удалить фильм из избранного - > ')
#     if choice == '1':
#         print(f'Ваш список избранных фильмов:', *liked_films, '\n')
#     elif choice == '2':
#         film = input('Введите название фильма: ')
#         if film in films:
#             if film not in liked_films:
#                 liked_films.append(film)
#                 print('Ваш фильм добавлен!\n')
#             else:
#                 print('Такой фильм у Вас уже есть\n')
#         else:
#             print('Такого фильма в наше библиотеке нет, добавим его позже\n')
#     elif choice == '3':
#         film = input('Введите название фильма, который вы хотите удалить: ')
#         if film in liked_films:
#             liked_films.remove(film)
#             print('Фильм удален\n')
#         else:
#             print('Такого фильма нет у Вас в избранном\n')
#     else:
#         print('До новых встреч!')
#         break


# numbers = [1, 23, 54, 76, 3, 22]
#
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))


# # Задание 2
#
# numbers = input('Введите список чисел через пробел: ').split()
# find_number = input('Введите число, которое вы хотите найти: ')
# count_number = 0
# print(numbers)
#
# for i_count in numbers:
#     if find_number == i_count:
#         count_number += 1
# print(f'Количесвто {find_number} в списке: {count_number}')

# #  Задание 2 через метод
#
# numbers = input('Введите список чисел через пробел: ').split()
# find_number = input('Введите число, которое вы хотите найти: ')
# print(f'Количесвто {find_number} в списке: {numbers.count(find_number)}')

# # Задание 3
#
# numbers_list = list(map(int, input('Введите числа через пробел: ').split()))
#
# print(f'Сумма всех чисел списка: {sum(numbers_list)}')
# print(f'Среднее арифметическое всех чисел списка: {sum(numbers_list) /  len(numbers_list)}')

# # Задание 3 через цикл
#
# numbers_list = list(map(int, input('Введите числа через пробел: ').split()))
# count_number = 0
# sum_num = 0
#
# for i_num in numbers_list:
#     count_number += 1
#     sum_num += i_num
# print(f'Сумма всех чисел в списке: {sum_num}\n'
#       f'Среднее арифметическое всех чисел списка: {sum_num /  count_number}')





