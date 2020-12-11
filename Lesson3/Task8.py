# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

my_list = []

for i in range(0,4):
    sum = 0
    my_list.append([])
    for ii in range(0,4):
        x = int(input(f'Введите {ii+1} число: '))
        sum += x
        my_list[i].append(x)
    my_list[i].append(sum)

for i in my_list:
    for ii in i:
        print(f'{ii:>4}', end='')
    print()