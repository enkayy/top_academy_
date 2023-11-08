# # Задание 1
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
#
# summ_even = 0
# summ_odd = 0
# summ_9 = 0
#
# count_even = 0
# count_odd = 0
# count_9 = 0
#
# for i in range(start, end + 1):
#
#     if i % 2 == 0:
#         summ_even += i
#         count_even += 1
#     else:
#         summ_odd += i
#         count_odd += 1
#
#     if i % 9 == 0:
#         summ_9 += i
#         count_9 += 1
#
#
# print(f'Сумма и среднеарифметическое четных чисел в диапазоне соответственно: {summ_even}, {summ_even / count_even}')
# print(f'Сумма и среднеарифметическое нечетных чисел в диапазоне соответственно: {summ_odd}, {summ_odd / count_odd}')
# print(f'Сумма и среднеарифметическое чисел в диапазоне кратных 9 соответственно: {summ_9}, {summ_9 / count_9}')


# # Задание 2
#
# lenght = int(input('Введите количество символов: '))
# symbol = input('Введите символ: ')
#
# for i in range(lenght):
#     print(symbol, end='\n')

# # Задание 3
#
# for i in range(1, 100):
#     number = int(input('Введите число (7 для выхода): '))
#     if number == 7:
#         print('Завершаем работу программы...')
#         break
#     elif number > 0:
#         print('Numberis positive\n')
#     elif number < 0:
#         print('Numberis negative\n')
#     elif number == 0:
#         print('Number is equal to zero\n')
#
#     if i == 99:
#         print('Все попытки были использованы')
