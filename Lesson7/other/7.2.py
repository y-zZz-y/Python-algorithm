"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def mergesort(mas):
    if len(mas) > 1:
        mid = len(mas) // 2
        lefthalf = mas[:mid]
        righthalf = mas[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mas[k] = lefthalf[i]
                i = i + 1
            else:
                mas[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            mas[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            mas[k] = righthalf[j]
            j = j + 1
            k = k + 1


massive = [random.randint(0, 50) for _ in range(10)]
print(f"Исходный массив: {massive}")
mergesort(massive)
print(f"Отсортированный массив: {massive}")
