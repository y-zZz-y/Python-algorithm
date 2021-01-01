# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

size = 10

start = 1

visited = [False] * (size + 1)
prev = [None] * (size + 1)

def graph_gen(vertex):
    vert = [i for i in range(vertex)]
    graph = [[] for _ in range(vertex)]

    for i in vert:
        vert_ch = random.choices(vert, k=random.randint(1, vertex))
        vert_ch = set(vert_ch)
        vert_ch.discard(i)
        graph[i] = list(vert_ch)

    return graph


def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)


g = graph_gen(size)
dfs(start, visited, prev, g)

