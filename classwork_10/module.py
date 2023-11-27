# def function_1(a, b, *args):  # *args (неименованный элемент) нужно для, чтобы передавать больше заданных элементов
#     print(a, b, args)
#
#
# function_1(1, 2, 2, 3, 5, 6, 7, 8)  # неименованные элементы выводятся в скобках


# def summa(*args):
#     # counter = 0
#     # for i_arg in args:
#     #     counter += i_arg
#     # return counter
#     try:
#         return sum(args)  # Это картеж, тоже, что и список, только он неизменяеммый
#     except TypeError:  # обрабатываем ошибку, если формат данных неправильный
#         return 'Неверный формат данных'
#
#
# print(summa(1, 2, 3, '4', 5, 6, 7, 8, 9, 10))


# # <input name='surname'>
# # <input name='email'>
#
# def get_form(**kwargs):  # Именнованый аргумент, аргументы по ключу
# # def get_form(name, email):  # Позиционный элемент
# #     print(kwargs)
#     print(kwargs['name'])  # поиск по ключу в словаре
#
# get_form(name='ivanov', email='ivanov@mail.ru')  # ключ и значение


# def get(request, *args, **kwargs):
#     print(f'Сделан запрос на {request}')
#     print(f'Параметры запроса {kwargs["cache_control"]}')
#     print(f'Относительный путь: {args[0]}')  # В кортеже можно брать значения по индексу
#
#
# get('http://test.ru', '/page_1', cache_control='no-cache', control_type='text/html')


# def get_group(group_num, degree, year, *args):
#     count = 0
#     print(f'Номер группы: {group_num}\n'
#           f'Степень: {degree}\n'
#           f'Год выпуска: {year}')
#     for i_stud in args:
#         count += 1
#         print(f'{count}. {i_stud}')
#     # for i_stud in range(len(args)):
#     #     print(f'{i_stud + 1}. {args[i_stud]}')
#
#
# get_group('Фт-200007', 'бакалавр', 2023, 'Падурин', 'Габитов', 'Иванов')


# # <input type="email" name='email' required>
# # <input type="tel" name='phone' required>
# # <input type="text" name='name'>
# # <input type="text" name='surname'>
#
# def reg(**kwargs):
#     try:
#         if kwargs['email'] != 0 and kwargs['tel'] != 0:
#             print(f'Email: {kwargs["email"]}')
#             print(f'Tel: {kwargs["tel"]}')
#
#             if 'name' in kwargs:
#                 print(f'Name: {kwargs["name"]}')
#             else:
#                 pass
#
#             if 'surname' in kwargs:
#                 print(f'Surname: {kwargs["surname"]}')
#             else:
#                 pass
#     except KeyError:
#         print('Введены не все данные')
#
#
# reg(email='padura@mail.ru', tel='+79126666666', name='Marat')
# # На телефоне фотка с более емким решением и использованием доп. функции


# --- Анонимные функции --- #

# square = lambda x, y: x ** y  # lambda - вызов анонимной функции x(переменная, можно несколько): что делаем с ней
#
# print(square(5, 3))

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# square_num_list = [i ** 2 for i in nums_list]
# print(square_num_list)
#
# square_num_list_2 = map(lambda x: x ** 2, nums_list)  # меньше памяти занимает, если не прописовать list
# print(square_num_list_2)
# # for i in square_num_list_2:
# #     print(i)
#
# import sys
#
# print(sys.getsizeof(square_num_list_2))
# print(sys.getsizeof(square_num_list))
#
# print(next(square_num_list_2))  # как map можно применить функции next и он также является иттерируемым объектом
# print(next(square_num_list_2))
# print(next(square_num_list_2))
# print(next(square_num_list_2))

# import time
#
# class Iterator:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         print('__iter__')
#
#     def __next__(self):
#         print('__next__')
#         time.sleep(1)
#         self._n += 1
#         print(self._n)
#
# for i in Iterator(0):
#     pass


# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# filtered_list = list(filter(lambda x: x > 4, nums_list))  # Можно пройтись списком filter убирает элементы из списка,
# # а map применяет функцию на эелементы списка
#
# print(filtered_list)

# names_list = ['Ivan', 'Padura', 'Marat', 'Irina']
#
# filtered_list = list(filter(lambda x: x[0].lower() == 'i' and len(x) <= 4, names_list))
# print(filtered_list)

# nums = [123, 23423, 34, 8, 123, 459]
#
# filtered_nums_str = list(filter(lambda x: len(str(x)) == 3, nums))
# filtered_nums_map = list(map(int, (filter(lambda x: len(x) == 3, map(str, nums)))))
# filtered_nums = list(filter(lambda x: 99 < x < 1000, nums))
#
# print(filtered_nums_str)
# print(filtered_nums_map)
# print(filtered_nums)

students = [
    ["std 1", 4.5],
    ["std 9", 5],
    ["std 3", 3.3],
    ["std 7", 4.3],
    ["std 5", 4.7],
    ["std 22", 4.3],
    ["std 2", 4.3],
    ["std 43", 4.3],
    ["std 90", 4.3],
]

students_sorted_num = sorted(students, key=lambda x: x[1])
print(students_sorted_num)

students_sorted_list = sorted(students, key=lambda x: int(x[0].split()[1]))
print(students_sorted_list)
