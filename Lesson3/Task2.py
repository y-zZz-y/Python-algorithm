# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

my_list = [8, 3, 15, 6, 4, 2]
my_index = []

for i, ii in enumerate(my_list):
    if ii%2 == 0:
        my_index.append(i)

print(my_index)