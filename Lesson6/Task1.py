# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.

import sys

print(sys.version, sys.platform)

#3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)
#[Clang 6.0 (clang-600.0.57)] darwin

def show_size(x, level=0):
    print('\t'*level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x,str):
            for xx in x:
                show_size(xx, level + 1)

def show_size_sum(*args, print_all=False):
    size_sum = 0
    for i in args:
        size_sum += sys.getsizeof(i)
        if print_all:
            show_size(i, level=0)
    print('*'*20, f'ИТОГО: {size_sum}', '*'*20)



from random import randint

def replace_min_max(my_range):# ******************** ИТОГО: 592 ********************
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list_min = my_list_max = 0

    for i, ii in enumerate(my_list):
        if my_list[my_list_min] > ii:
            my_list_min = i
        if my_list[my_list_max] < ii:
            my_list_max = i

    my_list[my_list_min], my_list[my_list_max] = my_list[my_list_max], my_list[my_list_min]

    show_size_sum(my_list,my_list_min,my_list_max,enumerate(my_list), print_all=True)


def replace_min_max2(my_range):  #САМЫЙ БЫСТРЫЙ СПОСОБ # ******************** ИТОГО: 528 ********************
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list_min = my_list.index(min(my_list))
    my_list_max = my_list.index(max(my_list))

    my_list[my_list_min], my_list[my_list_max] = my_list[my_list_max], my_list[my_list_min]

    show_size_sum(my_list, my_list_min, my_list_max, print_all=True)

def replace_min_max3(my_range): #САМЫЙ ЭКОНОМНЫЙ СПОСОБ ПО ПАМЯТИ # ******************** ИТОГО: 472 ********************
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list[my_list.index(min(my_list))], my_list[my_list.index(max(my_list))] = my_list[my_list.index(max(my_list))], my_list[my_list.index(min(my_list))]

    show_size_sum(my_list, print_all=True)

replace_min_max(50)
#  type = <class 'list'>, size = 472, object = [852, 220, 78, 734, 681, 343, 978, 498, 561, 166, 208, 673, 204, 953, 848, 691, 335, 641, 652, 266, 36, 191, 763, 454, 731, 303, 881, 741, 493, 269, 262, 692, 230, 7, 536, 0, 274, 121, 835, 869, 330, 106, 204, 596, 288, 831, 936, 592, 92, 879]
# 	 type = <class 'int'>, size = 28, object = 852
# 	 type = <class 'int'>, size = 28, object = 220
# 	 type = <class 'int'>, size = 28, object = 78
# 	 type = <class 'int'>, size = 28, object = 734
# 	 type = <class 'int'>, size = 28, object = 681
# 	 type = <class 'int'>, size = 28, object = 343
# 	 type = <class 'int'>, size = 28, object = 978
# 	 type = <class 'int'>, size = 28, object = 498
# 	 type = <class 'int'>, size = 28, object = 561
# 	 type = <class 'int'>, size = 28, object = 166
# 	 type = <class 'int'>, size = 28, object = 208
# 	 type = <class 'int'>, size = 28, object = 673
# 	 type = <class 'int'>, size = 28, object = 204
# 	 type = <class 'int'>, size = 28, object = 953
# 	 type = <class 'int'>, size = 28, object = 848
# 	 type = <class 'int'>, size = 28, object = 691
# 	 type = <class 'int'>, size = 28, object = 335
# 	 type = <class 'int'>, size = 28, object = 641
# 	 type = <class 'int'>, size = 28, object = 652
# 	 type = <class 'int'>, size = 28, object = 266
# 	 type = <class 'int'>, size = 28, object = 36
# 	 type = <class 'int'>, size = 28, object = 191
# 	 type = <class 'int'>, size = 28, object = 763
# 	 type = <class 'int'>, size = 28, object = 454
# 	 type = <class 'int'>, size = 28, object = 731
# 	 type = <class 'int'>, size = 28, object = 303
# 	 type = <class 'int'>, size = 28, object = 881
# 	 type = <class 'int'>, size = 28, object = 741
# 	 type = <class 'int'>, size = 28, object = 493
# 	 type = <class 'int'>, size = 28, object = 269
# 	 type = <class 'int'>, size = 28, object = 262
# 	 type = <class 'int'>, size = 28, object = 692
# 	 type = <class 'int'>, size = 28, object = 230
# 	 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'int'>, size = 28, object = 536
# 	 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'int'>, size = 28, object = 274
# 	 type = <class 'int'>, size = 28, object = 121
# 	 type = <class 'int'>, size = 28, object = 835
# 	 type = <class 'int'>, size = 28, object = 869
# 	 type = <class 'int'>, size = 28, object = 330
# 	 type = <class 'int'>, size = 28, object = 106
# 	 type = <class 'int'>, size = 28, object = 204
# 	 type = <class 'int'>, size = 28, object = 596
# 	 type = <class 'int'>, size = 28, object = 288
# 	 type = <class 'int'>, size = 28, object = 831
# 	 type = <class 'int'>, size = 28, object = 936
# 	 type = <class 'int'>, size = 28, object = 592
# 	 type = <class 'int'>, size = 28, object = 92
# 	 type = <class 'int'>, size = 28, object = 879
#  type = <class 'int'>, size = 28, object = 6
#  type = <class 'int'>, size = 28, object = 35
#  type = <class 'enumerate'>, size = 64, object = <enumerate object at 0x7fc1e11da1c0>
# 	 type = <class 'tuple'>, size = 56, object = (0, 852)
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 852
# 	 type = <class 'tuple'>, size = 56, object = (1, 220)
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 220
# 	 type = <class 'tuple'>, size = 56, object = (2, 78)
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 78
# 	 type = <class 'tuple'>, size = 56, object = (3, 734)
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 734
# 	 type = <class 'tuple'>, size = 56, object = (4, 681)
# 		 type = <class 'int'>, size = 28, object = 4
# 		 type = <class 'int'>, size = 28, object = 681
# 	 type = <class 'tuple'>, size = 56, object = (5, 343)
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 343
# 	 type = <class 'tuple'>, size = 56, object = (6, 978)
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 978
# 	 type = <class 'tuple'>, size = 56, object = (7, 498)
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 498
# 	 type = <class 'tuple'>, size = 56, object = (8, 561)
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 561
# 	 type = <class 'tuple'>, size = 56, object = (9, 166)
# 		 type = <class 'int'>, size = 28, object = 9
# 		 type = <class 'int'>, size = 28, object = 166
# 	 type = <class 'tuple'>, size = 56, object = (10, 208)
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 208
# 	 type = <class 'tuple'>, size = 56, object = (11, 673)
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 673
# 	 type = <class 'tuple'>, size = 56, object = (12, 204)
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 204
# 	 type = <class 'tuple'>, size = 56, object = (13, 953)
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 953
# 	 type = <class 'tuple'>, size = 56, object = (14, 848)
# 		 type = <class 'int'>, size = 28, object = 14
# 		 type = <class 'int'>, size = 28, object = 848
# 	 type = <class 'tuple'>, size = 56, object = (15, 691)
# 		 type = <class 'int'>, size = 28, object = 15
# 		 type = <class 'int'>, size = 28, object = 691
# 	 type = <class 'tuple'>, size = 56, object = (16, 335)
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 335
# 	 type = <class 'tuple'>, size = 56, object = (17, 641)
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 641
# 	 type = <class 'tuple'>, size = 56, object = (18, 652)
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 652
# 	 type = <class 'tuple'>, size = 56, object = (19, 266)
# 		 type = <class 'int'>, size = 28, object = 19
# 		 type = <class 'int'>, size = 28, object = 266
# 	 type = <class 'tuple'>, size = 56, object = (20, 36)
# 		 type = <class 'int'>, size = 28, object = 20
# 		 type = <class 'int'>, size = 28, object = 36
# 	 type = <class 'tuple'>, size = 56, object = (21, 191)
# 		 type = <class 'int'>, size = 28, object = 21
# 		 type = <class 'int'>, size = 28, object = 191
# 	 type = <class 'tuple'>, size = 56, object = (22, 763)
# 		 type = <class 'int'>, size = 28, object = 22
# 		 type = <class 'int'>, size = 28, object = 763
# 	 type = <class 'tuple'>, size = 56, object = (23, 454)
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 28, object = 454
# 	 type = <class 'tuple'>, size = 56, object = (24, 731)
# 		 type = <class 'int'>, size = 28, object = 24
# 		 type = <class 'int'>, size = 28, object = 731
# 	 type = <class 'tuple'>, size = 56, object = (25, 303)
# 		 type = <class 'int'>, size = 28, object = 25
# 		 type = <class 'int'>, size = 28, object = 303
# 	 type = <class 'tuple'>, size = 56, object = (26, 881)
# 		 type = <class 'int'>, size = 28, object = 26
# 		 type = <class 'int'>, size = 28, object = 881
# 	 type = <class 'tuple'>, size = 56, object = (27, 741)
# 		 type = <class 'int'>, size = 28, object = 27
# 		 type = <class 'int'>, size = 28, object = 741
# 	 type = <class 'tuple'>, size = 56, object = (28, 493)
# 		 type = <class 'int'>, size = 28, object = 28
# 		 type = <class 'int'>, size = 28, object = 493
# 	 type = <class 'tuple'>, size = 56, object = (29, 269)
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 28, object = 269
# 	 type = <class 'tuple'>, size = 56, object = (30, 262)
# 		 type = <class 'int'>, size = 28, object = 30
# 		 type = <class 'int'>, size = 28, object = 262
# 	 type = <class 'tuple'>, size = 56, object = (31, 692)
# 		 type = <class 'int'>, size = 28, object = 31
# 		 type = <class 'int'>, size = 28, object = 692
# 	 type = <class 'tuple'>, size = 56, object = (32, 230)
# 		 type = <class 'int'>, size = 28, object = 32
# 		 type = <class 'int'>, size = 28, object = 230
# 	 type = <class 'tuple'>, size = 56, object = (33, 7)
# 		 type = <class 'int'>, size = 28, object = 33
# 		 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'tuple'>, size = 56, object = (34, 536)
# 		 type = <class 'int'>, size = 28, object = 34
# 		 type = <class 'int'>, size = 28, object = 536
# 	 type = <class 'tuple'>, size = 56, object = (35, 0)
# 		 type = <class 'int'>, size = 28, object = 35
# 		 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'tuple'>, size = 56, object = (36, 274)
# 		 type = <class 'int'>, size = 28, object = 36
# 		 type = <class 'int'>, size = 28, object = 274
# 	 type = <class 'tuple'>, size = 56, object = (37, 121)
# 		 type = <class 'int'>, size = 28, object = 37
# 		 type = <class 'int'>, size = 28, object = 121
# 	 type = <class 'tuple'>, size = 56, object = (38, 835)
# 		 type = <class 'int'>, size = 28, object = 38
# 		 type = <class 'int'>, size = 28, object = 835
# 	 type = <class 'tuple'>, size = 56, object = (39, 869)
# 		 type = <class 'int'>, size = 28, object = 39
# 		 type = <class 'int'>, size = 28, object = 869
# 	 type = <class 'tuple'>, size = 56, object = (40, 330)
# 		 type = <class 'int'>, size = 28, object = 40
# 		 type = <class 'int'>, size = 28, object = 330
# 	 type = <class 'tuple'>, size = 56, object = (41, 106)
# 		 type = <class 'int'>, size = 28, object = 41
# 		 type = <class 'int'>, size = 28, object = 106
# 	 type = <class 'tuple'>, size = 56, object = (42, 204)
# 		 type = <class 'int'>, size = 28, object = 42
# 		 type = <class 'int'>, size = 28, object = 204
# 	 type = <class 'tuple'>, size = 56, object = (43, 596)
# 		 type = <class 'int'>, size = 28, object = 43
# 		 type = <class 'int'>, size = 28, object = 596
# 	 type = <class 'tuple'>, size = 56, object = (44, 288)
# 		 type = <class 'int'>, size = 28, object = 44
# 		 type = <class 'int'>, size = 28, object = 288
# 	 type = <class 'tuple'>, size = 56, object = (45, 831)
# 		 type = <class 'int'>, size = 28, object = 45
# 		 type = <class 'int'>, size = 28, object = 831
# 	 type = <class 'tuple'>, size = 56, object = (46, 936)
# 		 type = <class 'int'>, size = 28, object = 46
# 		 type = <class 'int'>, size = 28, object = 936
# 	 type = <class 'tuple'>, size = 56, object = (47, 592)
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 28, object = 592
# 	 type = <class 'tuple'>, size = 56, object = (48, 92)
# 		 type = <class 'int'>, size = 28, object = 48
# 		 type = <class 'int'>, size = 28, object = 92
# 	 type = <class 'tuple'>, size = 56, object = (49, 879)
# 		 type = <class 'int'>, size = 28, object = 49
# 		 type = <class 'int'>, size = 28, object = 879
# ******************** ИТОГО: 592 ********************

replace_min_max2(50)
#  type = <class 'list'>, size = 472, object = [837, 57, 542, 454, 239, 731, 410, 922, 541, 656, 898, 272, 885, 148, 513, 438, 629, 966, 973, 183, 974, 286, 765, 541, 896, 396, 991, 469, 318, 25, 745, 722, 138, 153, 796, 253, 319, 807, 362, 654, 166, 256, 374, 378, 664, 815, 763, 375, 178, 919]
# 	 type = <class 'int'>, size = 28, object = 837
# 	 type = <class 'int'>, size = 28, object = 57
# 	 type = <class 'int'>, size = 28, object = 542
# 	 type = <class 'int'>, size = 28, object = 454
# 	 type = <class 'int'>, size = 28, object = 239
# 	 type = <class 'int'>, size = 28, object = 731
# 	 type = <class 'int'>, size = 28, object = 410
# 	 type = <class 'int'>, size = 28, object = 922
# 	 type = <class 'int'>, size = 28, object = 541
# 	 type = <class 'int'>, size = 28, object = 656
# 	 type = <class 'int'>, size = 28, object = 898
# 	 type = <class 'int'>, size = 28, object = 272
# 	 type = <class 'int'>, size = 28, object = 885
# 	 type = <class 'int'>, size = 28, object = 148
# 	 type = <class 'int'>, size = 28, object = 513
# 	 type = <class 'int'>, size = 28, object = 438
# 	 type = <class 'int'>, size = 28, object = 629
# 	 type = <class 'int'>, size = 28, object = 966
# 	 type = <class 'int'>, size = 28, object = 973
# 	 type = <class 'int'>, size = 28, object = 183
# 	 type = <class 'int'>, size = 28, object = 974
# 	 type = <class 'int'>, size = 28, object = 286
# 	 type = <class 'int'>, size = 28, object = 765
# 	 type = <class 'int'>, size = 28, object = 541
# 	 type = <class 'int'>, size = 28, object = 896
# 	 type = <class 'int'>, size = 28, object = 396
# 	 type = <class 'int'>, size = 28, object = 991
# 	 type = <class 'int'>, size = 28, object = 469
# 	 type = <class 'int'>, size = 28, object = 318
# 	 type = <class 'int'>, size = 28, object = 25
# 	 type = <class 'int'>, size = 28, object = 745
# 	 type = <class 'int'>, size = 28, object = 722
# 	 type = <class 'int'>, size = 28, object = 138
# 	 type = <class 'int'>, size = 28, object = 153
# 	 type = <class 'int'>, size = 28, object = 796
# 	 type = <class 'int'>, size = 28, object = 253
# 	 type = <class 'int'>, size = 28, object = 319
# 	 type = <class 'int'>, size = 28, object = 807
# 	 type = <class 'int'>, size = 28, object = 362
# 	 type = <class 'int'>, size = 28, object = 654
# 	 type = <class 'int'>, size = 28, object = 166
# 	 type = <class 'int'>, size = 28, object = 256
# 	 type = <class 'int'>, size = 28, object = 374
# 	 type = <class 'int'>, size = 28, object = 378
# 	 type = <class 'int'>, size = 28, object = 664
# 	 type = <class 'int'>, size = 28, object = 815
# 	 type = <class 'int'>, size = 28, object = 763
# 	 type = <class 'int'>, size = 28, object = 375
# 	 type = <class 'int'>, size = 28, object = 178
# 	 type = <class 'int'>, size = 28, object = 919
#  type = <class 'int'>, size = 28, object = 26
#  type = <class 'int'>, size = 28, object = 29
# ******************** ИТОГО: 528 ********************

replace_min_max3(50)
#  type = <class 'list'>, size = 472, object = [166, 337, 599, 625, 705, 222, 256, 46, 129, 430, 2, 272, 95, 555, 974, 310, 254, 416, 875, 414, 998, 467, 907, 698, 466, 143, 201, 273, 442, 306, 994, 508, 871, 914, 103, 711, 782, 304, 334, 46, 523, 299, 159, 221, 748, 55, 317, 427, 220, 342]
# 	 type = <class 'int'>, size = 28, object = 166
# 	 type = <class 'int'>, size = 28, object = 337
# 	 type = <class 'int'>, size = 28, object = 599
# 	 type = <class 'int'>, size = 28, object = 625
# 	 type = <class 'int'>, size = 28, object = 705
# 	 type = <class 'int'>, size = 28, object = 222
# 	 type = <class 'int'>, size = 28, object = 256
# 	 type = <class 'int'>, size = 28, object = 46
# 	 type = <class 'int'>, size = 28, object = 129
# 	 type = <class 'int'>, size = 28, object = 430
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 272
# 	 type = <class 'int'>, size = 28, object = 95
# 	 type = <class 'int'>, size = 28, object = 555
# 	 type = <class 'int'>, size = 28, object = 974
# 	 type = <class 'int'>, size = 28, object = 310
# 	 type = <class 'int'>, size = 28, object = 254
# 	 type = <class 'int'>, size = 28, object = 416
# 	 type = <class 'int'>, size = 28, object = 875
# 	 type = <class 'int'>, size = 28, object = 414
# 	 type = <class 'int'>, size = 28, object = 998
# 	 type = <class 'int'>, size = 28, object = 467
# 	 type = <class 'int'>, size = 28, object = 907
# 	 type = <class 'int'>, size = 28, object = 698
# 	 type = <class 'int'>, size = 28, object = 466
# 	 type = <class 'int'>, size = 28, object = 143
# 	 type = <class 'int'>, size = 28, object = 201
# 	 type = <class 'int'>, size = 28, object = 273
# 	 type = <class 'int'>, size = 28, object = 442
# 	 type = <class 'int'>, size = 28, object = 306
# 	 type = <class 'int'>, size = 28, object = 994
# 	 type = <class 'int'>, size = 28, object = 508
# 	 type = <class 'int'>, size = 28, object = 871
# 	 type = <class 'int'>, size = 28, object = 914
# 	 type = <class 'int'>, size = 28, object = 103
# 	 type = <class 'int'>, size = 28, object = 711
# 	 type = <class 'int'>, size = 28, object = 782
# 	 type = <class 'int'>, size = 28, object = 304
# 	 type = <class 'int'>, size = 28, object = 334
# 	 type = <class 'int'>, size = 28, object = 46
# 	 type = <class 'int'>, size = 28, object = 523
# 	 type = <class 'int'>, size = 28, object = 299
# 	 type = <class 'int'>, size = 28, object = 159
# 	 type = <class 'int'>, size = 28, object = 221
# 	 type = <class 'int'>, size = 28, object = 748
# 	 type = <class 'int'>, size = 28, object = 55
# 	 type = <class 'int'>, size = 28, object = 317
# 	 type = <class 'int'>, size = 28, object = 427
# 	 type = <class 'int'>, size = 28, object = 220
# 	 type = <class 'int'>, size = 28, object = 342
# ******************** ИТОГО: 472 ********************
