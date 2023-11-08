# --- Теория множеств ---

# a = set()  # создать множество
# a.add('apple')  # добавить в множество
# a.add('banana')
# print(a[0])  # по индексу нельзя, потому что это неупорядоченная коллекция
# print('banana' in a)
# a.remove('apple')  # выкинет ошибку, если нет такого элемента
# a.discard('apple')  # не выкинет ошибку, если такого элемента нет
# a.pop()  # удалит рандомный элемент
# b = {'orange', 'watermelon', 'apple'}  # можно и так создать множество, только если там уже что-то есть

# print(a.intersection(b))  # пересечение, пустое множество, потому что нет пересечений
# print(a.difference(b))  # Разница
# print(b.difference(a))
# print(a.union(b))  # объединение

# c = a.union(b)  # создает новое, можно закинуть в отдельную переменную
# print(c)

# a.clear()  # Очистить множество
# print(a)

# a.update(b)  # обновляет текущее множество другим множеством
# print(a)

# for item in a:  # выводит в рандомном порядке
#     print(item)

# print(*a)  # можно распаковать
# print(' '.join(a))  # можно добавлять к строке

# set_1 = {['Name'], 18, {'key': 'value'}}  # могут храниться только простые типы данных числа, строки
# # захешировать списки и словари нельзя,
# print(set_1)

# import sys
#
# list_1 = ['apple', 'orange']
# set_1 = {'apple', 'orange'}
#
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(set_1))  # память больше потому что коллекция неупорядоченна

# print(set_1.update(list_1))  # вернется None, потому что разные типы данных

# l = 'asd'
# l = ['a', 'b', 'c']
# print(set(l))  # можно преобразовать строку и список


# Задание посчитать уникальные символы в файле
#
# with open('text.txt', 'r') as file:
#     text = file.read()
#     set_text = set(text)
#     print(len(set_text))


# Задание провести статистику по всем буквам и найти самую повторяющуюся из файла voyna-i-mir.txt
#
# data = {}
#
# with open('voyna-i-mir.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     symbols = set(text)
#     file.seek(0)
#     for sym in symbols:
#         if sym.isalpha():
#             data[sym] = text.count(sym)
#     sorted_dict = sorted(data, key=lambda x: data[x], reverse=True)  # сортировка по значению в словарю
#     print(data['о'])
#     print(data['а'])
# print(sorted_dict)
# print(data)


# Задание может ли строка стать палиндромом
#
# string = 'fdsfsfdsfdsf'
#
#
# def check(text):
#     data = {}
#     for i in text:
#         data.setdefault(i, 0)
#         data[i] += 1
#
#     count = 0
#     for j in data.values():
#         if j % 2 != 0:
#             count += 1
#     if count <= 1:
#         print('Может')
#     else:
#         print('Не может')
#
#
# check(string)


# -- Генераторы --

# import sys
#
# lis_1 = [i for i in range(100)]
# generation = (i for i in range(100))  # генераторное выражение,
# # которое на данный момент хранит текущее(одно) значение, но можно вызвать следующее
# # создан для экономии памяти. Можно там хранить элементы, а потом циклом пройтись чтобы записать их
# print(sys.getsizeof(lis_1))
# print(sys.getsizeof(generation))
# print(lis_1)
# print(generation)
#
# print(generation.__next__())
# print(generation.__next__())


# for i in generation:
#     print(i)


# def custom_range(start, end):
#     for i in range(start, end):
#         yield i
#
#
# for i in custom_range(10, 20):
#     print(i)


# class Generator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.cur = start
#
#     def __iter__(self):
#         print('__itter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         if self.cur == self.end:
#             raise StopIteration
#         self.cur += 1
#         return self.cur
#
#
# for i in Generator(10, 20):
#     print(i)


# with open('second_text.txt', 'r') as file:
#     words = (i_word for i_word in file.readlines())  # можно превратить в ту структуру данных, которая нам нужна
#     print(*words)  # есть распаковка

# for i in words:
#     print(i.strip())


# # сделать через генераторную функцию
#
#
# def generation_func():
#     with open('second_text.txt', 'r') as file:
#         for i in file.readlines():
#             yield i
#
#
# for i in generation_func():
#     print(i.strip())


# бесконечный генератор через генераторную функцию
#
#
# def infinite_gen():
#     while True:
#         yield 'asd'
#
#
# for i in infinite_gen():
#     print(i)


# list_1 = ['Tema', 'Irina', 'Stepa', 'Kosty']
# gen = (i for i in list_1 if 'a' not in i.lower())
# print(*gen)
#
# def names():
#     for i_word in list_1:
#         if 'a' in i_word:
#             yield i_word
#
#
# for i in names():
#     print(i)











