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


def dfs_my(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs_my(u, visited, prev, g)


g = graph_gen(size)
dfs_my(start, visited, prev, g)


###############################

def create_graph(vertex, percent=1.0):
    assert 0 < percent <= 1, 'Неверный диапазон'

    graph = {}

    for i in range(vertex):
        graph[i] = set()

        count_edge = random.randrange(1, int(vertex*percent))
        while len(graph[i]) < count_edge:
            edge = random.randrange(0,vertex)
            if edge !=i:
                graph[i].add(edge)

    return graph

def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    def _dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for item in graph[vertex]:
            if not is_visited[item]:
                parent[item] = vertex
                _dfs(item)
                path.append(vertex)
        else:
            path.append(-vertex)

    _dfs(start)

    return parent, path

g = create_graph(int(input('Сколько вершин будет в графе: ')), float(input('Укажите максимальное число ребер у вершины\n Процент от числа вершин (0; 1]: ')))

for key, value in g.items():
    print(f'Из вершины "{key}" ребра ведут к вершинам {value}')

while True:
    s = int(input('\nС какой вершины начать обход (-1 для выхода): '))
    if s == -1:
        break

    parent, path = dfs(g,s)
    print(parent)

    for i, vertex in enumerate(path):
        if i % 10 == 0:
            print()

        print(f'{vertex:>4};', end='')