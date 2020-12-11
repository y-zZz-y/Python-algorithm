# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.

from random import randint

matrix_range = 5
matrix = [[randint(0,100) for _ in range(matrix_range)] for _ in range(matrix_range)]

min = [i[0] for i in matrix]

for i, el in enumerate(matrix):
    for ii in el:
        if ii < min[i]:
            min[i] = ii
max = min[0]
for i in min:
    if i > max:
        max = i

for i in range(matrix_range):
    for ii in range(matrix_range):
        print(f'{matrix[ii][i]:>4}', end='')
    print()

print(f'Vаксимальный элемент среди минимальных элементов столбцов матрицы: {max}')