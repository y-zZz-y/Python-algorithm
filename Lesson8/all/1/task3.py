# Задание 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в
# котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from collections import deque
import random

# def graph_construction(n):
#     numb_vertex = list([i for i in range(0, n)])
#     graph = dict()
#
#     for i in range(0, n):
#         list_vertex = list()
#         for j in range(0, n):
#             if numb_vertex[j] != i:
#                 list_vertex.append(numb_vertex[j])
#         graph[i] = list_vertex
#     return graph

def graph_construction(n):
    numb_vertex = list([i for i in range(1, n)])
    graph = dict()
    for i in range(0, n):
        graph[i] = ""

    start = 0
    while numb_vertex:
        spam = random.choice(numb_vertex)
        numb_vertex.remove(spam)
        graph[start] = [spam]
        start = spam
    graph[start] = [0]
    return graph


def depth_first_search(graph, start):
    length = len(graph)
    is_visited = list()
    deq_vertex = deque()
    deq_vertex.append(start)

    while deq_vertex:
        vertex = deq_vertex.pop()
        is_visited.append(vertex)
        for i in graph[vertex]:
            if i not in deq_vertex and i not in is_visited:
                deq_vertex.append(i)

    return is_visited


n = int(input('Введите число вершин: '))
graph = graph_construction(n)
# более интересный пример для проверки, не все вршины связаны
# graph = {
#     0: {1, 2, 3},
#     1: {0, 2},
#     2: {0, 1, 4},
#     3: {2, 5},
#     4: {2, 5},
#     5: {3, 4}
# }
for k, v in graph.items():
    print(k, v)
start = int(input('Введите вершину откуда начинаем обход: '))
print(depth_first_search(graph, start))