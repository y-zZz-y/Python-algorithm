"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""

import random


def select_nth(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)


def median(items):
    if len(items) % 2:
        return select_nth(len(items) // 2, items)

    else:
        left = select_nth((len(items) - 1) // 2, items)
        right = select_nth((len(items) + 1) // 2, items)

        return (left + right) / 2


random_list = [random.randrange(1, 100) for _ in range(11)]
print(f"Исходный массив: {random_list}")
print(f"Медиана: {int(median(random_list))}")
