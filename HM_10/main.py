# # задание 4
#
# def min_num(a: int, b: int, c: int, d: int, e: int) -> int:
#     """
#     Возвращает минимальное число
#     :param a: int
#     :param b: int
#     :param c: int
#     :param d: int
#     :param e: int
#     :return: int
#     """
#     return min(a, b, c, d, e)
#
#
# print(min_num(123, 112, 43, 255, 932))


# # Задание 5
#
# def mult_in_range(start: int, end: int) -> int:
#     """
#     Вычисляет происведение всех чисел в диапазоне
#     :param start: int
#     :param end: int
#     :return: int
#     """
#     product = 1
#     if start > end:
#         change = start
#         start = end
#         end = change
#     for i_num in range(start, end + 1):
#         product *= i_num
#     return product
#
#
# print(mult_in_range(5, 1))


# # Задание 6
#
# def digits_in_num(a: int) -> int:
#     """
#     Считат кол-во цифр в числе
#     :param a: int
#     :return: int
#     """
#     return len(str(a))
#
#
# print(digits_in_num(3303))


# # Задание 7
#
# def palindrome_num(num: int) -> bool:
#     """
#     Проверяет является ли число палиндромом
#     :param num: int
#     :return: bool
#     """
#     str_num = str(num)
#     length_num = int(len(str_num) / 2)
#     if str_num[:length_num] == str_num[:length_num - 1:-1]:
#         return True
#     return False
#
#
# print(palindrome_num(12344321))
# print(palindrome_num(12344123))
