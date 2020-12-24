# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#
# Примечания:
#
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random

def bubble_sort(mylist):
    n = 1
    while n < len(mylist):
        replace = 0
        for i in range(len(mylist)-n):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i + 1] = mylist[i+1], mylist[i]
                replace += 1
        if not replace:
            return n
        else:
            n += 1
            print(n, mylist)


a = [i for i in range(-100,100)]
random.shuffle(a)
print('Unsorted list: ', a)
print(f'The list is sorted in {bubble_sort(a)} iterations')
