# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#
# Примечание. Идеальным решением будет:
#
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
#
# b. написать 3 варианта кода (один у вас уже есть),
#
# c. проанализировать 3 варианта и выбрать оптимальный,
#
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

from random import randint
import cProfile

def replace_min_max(my_range):
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list_min = my_list_max = 0

    for i, ii in enumerate(my_list):
        if my_list[my_list_min] > ii:
            my_list_min = i
        if my_list[my_list_max] < ii:
            my_list_max = i

    my_list[my_list_min], my_list[my_list_max] = my_list[my_list_max], my_list[my_list_min]

def replace_min_max2(my_range):  #САМЫЙ БЫСТРЫЙ СПОСОБ
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list_min = my_list.index(min(my_list))
    my_list_max = my_list.index(max(my_list))

    my_list[my_list_min], my_list[my_list_max] = my_list[my_list_max], my_list[my_list_min]

def replace_min_max3(my_range):
    my_list = [randint(0,1000) for el in range(my_range)]
    my_list[my_list.index(min(my_list))], my_list[my_list.index(max(my_list))] = my_list[my_list.index(max(my_list))], my_list[my_list.index(min(my_list))]


#Замеры производим в зависимости от длины списка
#Результат: replace_min_max2 - самый быстрый способ

#Test
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max(50)"
# 1000 loops, best of 3: 80.9 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max2(50)"
# 1000 loops, best of 3: 77.2 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max3(50)"
# 1000 loops, best of 3: 81.6 usec per loop

# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max(500)"
# 1000 loops, best of 3: 763 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max2(500)"
# 1000 loops, best of 3: 726 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max3(500)"
# 1000 loops, best of 3: 764 usec per loop

# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max(1000)"
# 1000 loops, best of 3: 1.5 msec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max2(1000)"
# 1000 loops, best of 3: 1.47 msec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task1" "Task1.replace_min_max3(1000)"
# 1000 loops, best of 3: 1.51 msec per loop


cProfile.run('replace_min_max(1000)')
cProfile.run('replace_min_max2(1000)')
cProfile.run('replace_min_max3(1000)')

# 5029 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Task1.py:4(replace_min_max)
#         1    0.000    0.000    0.003    0.003 Task1.py:5(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:334(randint)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1024    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          5035 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Task1.py:16(replace_min_max2)
#         1    0.000    0.000    0.002    0.002 Task1.py:17(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:334(randint)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1026    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
#          5033 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Task1.py:23(replace_min_max3)
#         1    0.000    0.000    0.003    0.003 Task1.py:24(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:334(randint)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1020    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('replace_min_max(100000)')
cProfile.run('replace_min_max2(100000)')
cProfile.run('replace_min_max3(100000)')

# 502296 function calls in 0.296 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.296    0.296 <string>:1(<module>)
#         1    0.015    0.015    0.295    0.295 Task1.py:4(replace_min_max)
#         1    0.042    0.042    0.280    0.280 Task1.py:5(<listcomp>)
#    100000    0.065    0.000    0.093    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.095    0.000    0.189    0.000 random.py:290(randrange)
#    100000    0.050    0.000    0.238    0.000 random.py:334(randint)
#         1    0.000    0.000    0.296    0.296 {built-in method builtins.exec}
#    100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    102291    0.017    0.000    0.017    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          502331 function calls in 0.250 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.250    0.250 <string>:1(<module>)
#         1    0.000    0.000    0.249    0.249 Task1.py:16(replace_min_max2)
#         1    0.034    0.034    0.244    0.244 Task1.py:17(<listcomp>)
#    100000    0.059    0.000    0.083    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.083    0.000    0.166    0.000 random.py:290(randrange)
#    100000    0.044    0.000    0.211    0.000 random.py:334(randint)
#         1    0.000    0.000    0.250    0.250 {built-in method builtins.exec}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
#    100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    102322    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
#          502213 function calls in 0.318 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.318    0.318 <string>:1(<module>)
#         1    0.000    0.000    0.315    0.315 Task1.py:23(replace_min_max3)
#         1    0.043    0.043    0.306    0.306 Task1.py:24(<listcomp>)
#    100000    0.072    0.000    0.106    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.103    0.000    0.209    0.000 random.py:290(randrange)
#    100000    0.054    0.000    0.263    0.000 random.py:334(randint)
#         1    0.000    0.000    0.318    0.318 {built-in method builtins.exec}
#         2    0.005    0.002    0.005    0.002 {built-in method builtins.max}
#         2    0.005    0.002    0.005    0.002 {built-in method builtins.min}
#    100000    0.014    0.000    0.014    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    102200    0.019    0.000    0.019    0.000 {method 'getrandbits' of '_random.Random' objects}
#         4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}