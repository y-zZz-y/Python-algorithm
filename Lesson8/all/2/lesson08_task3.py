"""Lesson 08 task 03"""
"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
 по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

import random

graph_length = 5


# linear graph generation
def graph_generation_linear(length):
    init_dict = {elem: [] for elem in range(0, length)}
    vertexes = [i for i in range(length)]

    elem = 0
    vertexes.pop(0)
    while True:
        if len(vertexes) == 0:
            break
        tmp = vertexes.pop(random.randint(0, len(vertexes) - 1))
        init_dict[elem] = [tmp]
        elem = tmp

    return init_dict


# branched graph generation
def graph_generation_branching(length):
    init_dict = {elem: [] for elem in range(0, length)}
    vertexes = [i for i in range(length)]
    vertexes.pop(0)

    for elem in init_dict.keys():
        tmp = []
        print(f"elem={elem}")
        array_len = len(vertexes)
        if array_len == 0:
            break
        elif array_len > 1:
            elements_amount = random.randint(1, array_len - 1)
        else:
            elements_amount = 1

        for i in range(0, elements_amount):
            chosen = random.choice(vertexes) # returns element
            index = vertexes.index(chosen) # returns index of element

            if index == -1:
                break
            if chosen in tmp:
                continue
            tmp.append(vertexes.pop(index))
        init_dict[elem] = tmp
    return init_dict


# g = graph_generation_linear(graph_length)
# print(g)

g = graph_generation_branching(graph_length)
print(g)


def dfs(visited, graph, node):
    if node not in visited:
        print(f"processing node {node}")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# g = {
#     0: [1, 2],
#     1: [3, 4],
#     2: [],
#     3: [],
#     4: []
# }

visited_nodes = set()
start_point = 0

dfs(visited_nodes, g, start_point)
print(visited_nodes)

