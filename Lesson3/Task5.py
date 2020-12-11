# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
#
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint

x = None
my_list = [randint(-100,100) for el in range(30)]
print(my_list)

for i, el in enumerate(my_list):
    if el < 0 and x == None:
        x = i
    elif el < 0 and el > my_list[x]:
        x = i

print(f'Максимальный отрицательный элемент: {my_list[x]}')
