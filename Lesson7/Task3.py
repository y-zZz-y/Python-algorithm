# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint

def find_mid(alist):

    mid = alist[len(alist) // 2]
    minlist = [i for i in alist if i <= mid]
    maxlist = [i for i in alist if i > mid]

    minlist.pop(minlist.index(mid))

    while not len(minlist) == len(maxlist):

        if len(minlist) > len(maxlist):
            maxlist.append(mid)
            mid = max(minlist)
            minlist.pop(minlist.index(mid))
        else:
            minlist.append(mid)
            mid = min(maxlist)
            maxlist.pop(maxlist.index(mid))
    else:
        return [minlist,mid,maxlist]

m = 10
alist = [randint(0,49) for _ in range(2*m+1)]
print(f'In list: {alist} - {len(alist)} elements')
print('{0} {1} {2}'.format(*find_mid(alist)))

