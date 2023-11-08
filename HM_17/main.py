# # Задание 1
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
#
# square_gen = (i_square ** 2 for i_square in range(start, end + 1))
#
# for i in square_gen:
#     print(i)


# # Задание 2
#
#
# def simple_num_gen_func(start, end):
#     for i_num in range(start, end + 1):
#         for i_del in range(2, i_num):
#             if i_num % i_del == 0:
#                 break
#         else:
#             yield i_num
#
#
# for i in simple_num_gen_func(1, 100):
#     print(i)


# # Задание 3
#
# class EvenNum:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.count = start - 1
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         if self.count == self.end:
#             raise StopIteration
#         self.count += 1
#         if self.count % 2 == 0:
#             return self.count
#
#
# for i in EvenNum(-20, 20):
#     print(i)

