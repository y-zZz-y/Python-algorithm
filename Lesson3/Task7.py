# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

my_list = [randint(0,100) for el in range(20)]
print(my_list)

min1 = min2 = 0

for i, el in enumerate(my_list):
    if el <= my_list[min1]:
        min2 = min1
        min1 = i

print(f'Первое минимальное с индексом {min1}:  {my_list[min1]}')
print(f'Второе минимальное с индексом {min2}:  {my_list[min2]}')