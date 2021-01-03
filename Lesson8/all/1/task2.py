# Задание 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список
# вершин, которые необходимо обойти.
from collections import deque

g = [
    [0, 0, 1, 1, 2, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    way = list()
    for i in range(0, length):
        way.append([])
        #way.append([start])
    start0 = start

    cost[start] = 0
    min_cost = 0
    deq = deque()

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    if way[i] == []:
                        if start != start0:
                            for j in range(len(way[start]) - 1):
                                way[i].append(way[start][j])
                    way[i].append(start)


        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                if way[i][-1] != start:
                    way[i].append(i)

    return cost, way

s = int(input('От какой вершины идти: '))
# print(dijkstra(g, s))
cost, way = dijkstra(g, s)
print(cost)
print(*way, sep='\n')