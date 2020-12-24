# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint

def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
        print(alist)


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            alist[k] = right[j]
            j += 1
            k += 1

size = 30
alist = [randint(0,49) for _ in range(size)]
print('Unsorted list: ', alist)
merge_sort(alist, 0, len(alist))
print('Sorted list: ', alist)
