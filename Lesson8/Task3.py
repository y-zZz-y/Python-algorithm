# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

def graph_gen(vertex):
    vert = [i for i in range(vertex)]
    graph = [[] for _ in range(vertex)]

    for i in vert:
        vert_ch = random.choices(vert, k=random.randint(1, vertex))
        vert_ch = set(vert_ch)
        vert_ch.discard(i)
        graph[i] = vert_ch

    return graph


print(graph_gen(8))