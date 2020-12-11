# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

my_list = [randint(0,100) for el in range(30)]
print(my_list)

min = max = 0
sum = 0

for i, el in enumerate(my_list):
    if el >= my_list[max]: # последнее максимальное в листе
        max = i
    if el < my_list[min]: # первое минимальное число в листе
        min = i

if min > max:
    min, max = max, min

for i in range(min+1,max):
    sum += my_list[i]
    print(my_list[i], end=' ')

print(f'\n{min} - {max} сумма {sum}')