# 3. Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану. Медианой называется
# элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.

import random

num_list_origin = [random.randint(0, 100) for i in range(2*random.randint(1, 10)+1)]
print(f'Исходный массив: {num_list_origin}')


def select_median(num_list):

    if len(num_list) % 2 == 1:
        return med(num_list, len(num_list) / 2)
    else:
        return 0.5 * (med(num_list, len(num_list)/2-1) +  med(num_list, len(num_list)/2))


def med(num_list, index):

    if len(num_list) == 1:
        return num_list[0]

    rnd_num = random.choice(num_list)

    lows = [i for i in num_list if i < rnd_num]
    highs = [i for i in num_list if i > rnd_num]
    rnd_indexes = [i for i in num_list if i == rnd_num]

    if index < len(lows):
        return med(lows, index)
    elif index < len(lows) + len(rnd_indexes):
        return rnd_indexes[0]
    else:
        return med(highs, index - len(lows) - len(rnd_indexes))

print(f'Медиана: {select_median(num_list_origin)}')