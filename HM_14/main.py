tuple_1 = (2, 3, 10, 23, 67)
tuple_2 = (67, 3, 33, 10, 89)
tuple_3 = (34, 3, 67, 77, 76)

# Задание 1

res = []

for i in tuple_1:
    if i in tuple_2 and i in tuple_3:
        res.append(i)
print(res)


# Задание 2
# не придумал другого способа, как определить уникальные элементы во всех массиывх, олько повторяющимся циклом
# можно записывать элементы в один список

res_1 = []
res_2 = []
res_3 = []

for i in tuple_1:
    if i not in tuple_2 and i not in tuple_3:
        res_1.append(i)

for i in tuple_2:
    if i not in tuple_3 and i not in tuple_1:
        res_2.append(i)

for i in tuple_3:
    if i not in tuple_1 and i not in tuple_2:
        res_3.append(i)

print(res_1)
print(res_2)
print(res_3)


# Задание 3

res = []

for i in range(len(tuple_1)):
    if tuple_1[i] == tuple_2[i] == tuple_3[i]:
        res.append(tuple_1[i])
print(res)
