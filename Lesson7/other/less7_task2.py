# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на
# экран исходный и отсортированный массивы.


import random

num_list_origin = [random.randint(0, 50) for i in range(10)]
print(f'Исходный массив: {num_list_origin}')

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list)//2
    left_list = merge_sort(num_list[:mid])
    right_list = merge_sort(num_list[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):

    sort_list = []
    left_index = 0
    right_index = 0

    for _ in range(len(left_list) + len(right_list)):
        if left_index == len(left_list):
            sort_list.append(right_list[right_index])
            right_index += 1
        elif right_index == len(right_list):
            sort_list.append((left_list[left_index]))
            left_index += 1
        else:
            if left_list[left_index] <= right_list[right_index]:
                sort_list.append((left_list[left_index]))
                left_index += 1
            else:
                sort_list.append(right_list[right_index])
                right_index += 1
    return sort_list

print(f'Отсортированый список: {merge_sort(num_list_origin)}')