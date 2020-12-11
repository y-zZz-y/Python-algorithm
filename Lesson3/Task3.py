# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

from random import randint

my_list = [randint(0,100) for el in range(30)]
print(my_list)
min = max = 0

for i, ii in enumerate(my_list):
    if my_list[min] > ii:
        min = i
    if my_list[max] < ii:
        max = i

print(f'минимальное число {my_list[min]} максимальное число {my_list[max]}')

my_list[min], my_list[max] = my_list[max], my_list[min]

print(my_list)