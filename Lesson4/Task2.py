import cProfile

def sieve(n):
    myrange = 4 if n < 2 else n**2+1

    s = [i for i in range(myrange)]
    s[1] = 0

    for i in range(2, myrange):
        if s[i] != 0:
            j = i*2
            while j < myrange:
                s[j] = 0
                j += i

    result = [i for i in s if i != 0]
    return result[n-1]


def prime(n):
    myrange = 4 if n < 2 else n ** 2 + 1
    s = [i for i in range(2,myrange)]

    for a in s:
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0):
            n -= 1
        if n <= 0:
            return a

#на первых числах быстрее prime, далее быстрее sieve

#Test

# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.sieve(1)"
# 1000 loops, best of 3: 2.19 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.sieve(10)"
# 1000 loops, best of 3: 27.5 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.sieve(50)"
# 1000 loops, best of 3: 836 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.sieve(100)"
# 1000 loops, best of 3: 3.48 msec per loop

# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.prime(1)"
# 1000 loops, best of 3: 1.27 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.prime(10)"
# 1000 loops, best of 3: 35.5 usec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.prime(50)"
# 1000 loops, best of 3: 1.3 msec per loop
# Jogger@MacBookPro Lesson4 % python -m timeit -n 1000 -s "import Task2" "Task2.prime(100)"
# 1000 loops, best of 3: 5.61 msec per loop

# cProfile.run('sieve(1)')
# cProfile.run('sieve(50)')
# cProfile.run('sieve(100)')

# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Task2.py:3(sieve)
#         1    0.000    0.000    0.000    0.000 Task2.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          6 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task2.py:16(<listcomp>)
#         1    0.001    0.001    0.001    0.001 Task2.py:3(sieve)
#         1    0.000    0.000    0.000    0.000 Task2.py:6(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          6 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task2.py:16(<listcomp>)
#         1    0.003    0.003    0.004    0.004 Task2.py:3(sieve)
#         1    0.001    0.001    0.001    0.001 Task2.py:6(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(1)')
# cProfile.run('prime(50)')
# cProfile.run('prime(100)')

# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task2.py:20(prime)
#         1    0.000    0.000    0.000    0.000 Task2.py:22(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Task2.py:20(prime)
#         1    0.000    0.000    0.000    0.000 Task2.py:22(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 Task2.py:20(prime)
#         1    0.001    0.001    0.001    0.001 Task2.py:22(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

