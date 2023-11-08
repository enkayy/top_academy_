from random import randint

list1 = []
list2 = []

for i in range(1, 15):
    list1.append(randint(-10, 15))
    list2.append(randint(-10, 15))

print(f'Первый список случайных чисел: {list1}')
print(f'Второй список случайных чисел: {list2}')

list3_1 = list1 + list2 # Содержит элементы двух списков
print(list3_1)

list3_2 = set(list3_1) # Список без повторяющихся значений
print(list3_2)

list3_3 = [i for i in list3_1 if i in list1 and i in list2] # Общее из 2-х списков
print(list3_3)

list3_4 = [i for i in list1 if i not in list2] + [i for i in list2 if i not in list1] # Уникальные числа в списке
print(list3_4)

list3_5 = min(list1), max(list1), min(list2), max(list2)
print(list3_5)


