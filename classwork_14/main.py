# --- Работа С файлами ---

# file = open('filename.txt', 'r')  # можно открыть на чтение 'r',
# file = open('filename.txt', 'w')  # запись 'w'
# file = open('filename.txt', 'a')  # дозапись 'a', append
# file = open('filename.txt', 'r+')  # можно открыть на чтение и дозапись 'r+'
# file = open('filename.txt', 'w+')  # можно открыть на чтение и запись 'w+', но файл сразу очистится
#
# file.write(f'Привет, Падура\n')
# file.write(f'Привет, я файл!\n')
#
# file.write(f'Ok\n')
# text = file.read()
# print(text)
#
# file.close()  # Закрытие файла

# file = open('filename.txt', 'r+')
#
# for _ in range(5):
#     file.write(f'Привет, я Падура!\n')
#
# file.close()


# file = open('filename.txt', 'r+')
# try:
#     text = file.readlines()  # читает файл по строкам, и выводит список
#     raise ValueError  # файл не успеет закрыться, если выйдет ошибка
#     # text = file.readlines()  # читает только первую строку
#     print(text)
# except ValueError:
#     print('Поймали ошибку')
# finally:  # выполняется в любом случа, несмотря на ошибку и конец кода
#     file.close()
#     print('Файл закрыт!')


# # filename_bin = open('file.bin', 'wb')  # 'wb' write binary
# filename_bin = open('file.bin', 'rb')  # 'rb' read binary
#
# # filename_bin.write(bytes('Какой-то текст'.encode()))  # нужно закодировать текст и перевести в байты
# print(filename_bin.read().decode())  # приставка b значит что строка закодирована, нужно декодировать
#
# filename_bin.close()


# with open('filename.txt', 'r') as file:  # Контекстный менеджер, который самостоятельно закрывает файл
#     print(file.read())

# class CustomFile:  # собственный контекстный менеджер, чтобы понять, как работает
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#
#     def __enter__(self):
#         print('Сработал метод __enter__')
#         self.file = open(self.file_name, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Сработал метод __exit__')
#         print(exc_type)
#         self.file.write(str(exc_tb))
#         self.file.close()
#         print('Файл закрыт')
#
#
# with CustomFile('filename.txt', 'w') as file:
#     file.write('Привет')

# with open('filename.txt', 'w') as file:
#     file.write('Привет')

# # Задача с шифром цезаря в файле
#
# from random import randint
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33]
#                        if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# with open('text.txt', 'w', encoding='utf-8') as file_1:  # можно сразу передавать кодировку
#     for _ in range(5):
#         file_1.write('Привет\n')
#
#
# # with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
# #     with open('text.txt', 'r', encoding='utf-8') as file_1:
# #         lines = file_1.readlines()
# #         for i_line in lines:
# #             shift = randint(1, 33)
# #             file_2.write(caesar_code(i_line.strip('\n'), shift) + '\n')
#
#
# with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         for i_line in lines:
#             shift = randint(1, 33)
#             ciphered = caesar_code(i_line.strip(), shift)
#             file_2.write(ciphered[:len(ciphered) // 2] + f'({shift})' + ciphered[len(ciphered) // 2:] + '\n')

# Задача 2

# frequency = {}
#
# csv - табличный вид файла
# with open('zen.txt', 'r+') as file:
#     text = file.read().lower()
#     # for i_sym in text:
#     #     if i_sym.isalpha():
#     #         frequency.setdefault(i_sym, text.count(i_sym))
#     # print(frequency)
#     # frequency = {sym: text.count(sym) for sym in text if sym.isalpha()}  # через генератор словаря
#     # alpha_num = len(frequency.keys())
#     # total_num = sum(frequency.values())
#     # min_alpha = min(frequency.values())
#     # max_alpha = max(frequency.values())
#     # file.seek(0)  # Стиавит курсов на конкретную позицию, readlines читает от курсора, когда файо уже открыт
#     # line_num = len(file.readlines())
#     # word_num = len(text.split())
#     #
#     # print(frequency)
#     # print(alpha_num)
#     # print(total_num)
#     # print(min_alpha)
#     # print(max_alpha)
#     # print(line_num)
#     # print(word_num)
#
#     file.seek(0)
#     reversed_text = file.readlines()[::-1]
#     # print(reversed_text)
#     for i_line in reversed_text:
#         file.write(i_line.strip() + '\n')
with open("bad_words.txt", "r") as file:
    with open("text_for_kid.txt", "r") as file_2:
        text = file_2.read()
        for bad in file.readlines():
            if bad.strip() in text:
                text = text.replace(bad, "")
    with open("text_for_kid.txt", "w") as file_2:
        file_2.write(text)
