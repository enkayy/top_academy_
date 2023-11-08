# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
#
# print(list_1 + list_2)  # Объединение списков
# print(list_1 * 2)  # Дублирование элементов
# print(list_2 - list_1)  # только умножение и сложение
# list_1.extend(list_2)  # Расширение первого списка элементами второго
# print(list_1)

# list_1 = ['1', '2', '3', '4']
# string = ''
# # new_string = string.join(list_1)  # передает в строку список, но только в если тип данных str
# for i in list_1:  # тоже самое, но сверху это делается в одну строчку
#     string += f'{i} '
# print(string)

# # List comprehension
# import sys
# list_1 = []
# list_2 = [i for i in range(1, 10)]  # Генерация списка
# list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1, 10):  # Тоже самое, что и сверху
#     list_1.append(i)
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(list_2))
# print(sys.getsizeof(list_3))

# list_2 = [i for i in range(1, 10) if i % 2 != 1]
# list_2 = [i ** 2 for i in range(1, 10) if i % 2 != 0]
# print(list_2)

# list_2 = [i for i in range(1, 5) for _ in range(5)]  # Чтобы сделать 5 дубликатов одного элемента
# print(list_2)
#
# list_2 = [[i for i in range(1, 5)] for _ in range(5)]  # Чтобы сделать 5 дубликатов одного списка
# print(list_2)
#
# list_2 = [i * j for i in range(1, 5) for j in range(1, 5)]  # Чтобы сделать 5 дубликатов умножения на разные j
# print(list_2)

# list_4 = [35, 4, 30, 7, 56]
# list_5 = [num for num in list_4 if num % 7 == 0]  # Выделить из списка 4 числа кратные 7
# print(list_5)

# import string
# letters = string.ascii_letters
#
# input_text = 'hell@o m#y n@a!me !is Ma@ra@t'
#
# letters_list = [letter for letter in input_text if (letter in letters or letter == ' ' or letter.isspace())]  # можно
# по разному проверять на пробел
# print(letters_list)
# print(''.join(letters_list))

# import string
#
# digits = string.digits
# input_text = '123sdf4213sdf4 sdfsdf234asd23sd234'
#
# digit_list = [num for num in input_text if num in digits]
#
# print(''.join(digit_list))
# print(len(digit_list))

# students = [
#     ['Петров', 4.5],
#     ['Иванов', 3.5],
#     ['Падурин', 4.6],
#     ['Габитов', 4.6],
#     ['Маркелов', 3.9],
# ]
#
# students_2 = [student for student in students if student[1] >= 4.5]
# print(students_2)

# Контрольная

# Задача 1

