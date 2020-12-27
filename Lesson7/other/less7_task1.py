# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите
# на экран исходный и отсортированный массивы.

import random

num_list_origin = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный массив: {num_list_origin}')


def bubble_sort(num_list):
    n = 1
    while n < len(num_list):
        k = 0
        for i in range(len(num_list) - n):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                k = i
        if not k:  # остановка глобальное цикла если не было обмена элементов
            break
        n += 1
    return num_list


print(f'Отсортированый список: {bubble_sort(num_list_origin)}')