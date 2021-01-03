"""Lesson 08 task 2"""
"""2. Доработать алгоритм Дейкстры (рассматривался на уроке), 
чтобы он дополнительно возвращал список вершин, которые необходимо обойти."""

import random
gh = [
    #0 1 2 3 4 5 6 7
    [0,0,1,1,9,0,0,0], #0
    [0,0,9,4,0,0,5,0], #1
    [0,9,0,0,3,0,6,0], #2
    [0,0,0,0,0,0,0,0], #3
    [0,0,0,0,0,0,1,0], #4
    [0,0,0,0,0,0,5,0], #5
    [0,0,7,0,8,1,0,0], #6
    [0,0,0,0,0,1,2,0], #7
]
qty = 5
# gh = [[random.randint(0, 2) * random.randint(0, 5) for _ in range(qty)] for _ in range(qty)]
print(*gh, sep='\n')


def alg_dik(graph, current_point):
    # create variables
    # is_visited  -list of visited nodes
    # cost - list of distances between nodes (wages)
    # init_point is needed for printing of routes
    #  parents list of nodes which are parent for current one
    length = len(graph)
    init_point = current_point
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[current_point] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[current_point] = True

        for i, vertex in enumerate(graph[current_point]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[current_point]:
                    cost[i] = vertex + cost[current_point]
                    parent[i] = current_point
        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                current_point = i

    path(cost, parent, init_point)
    return cost


def route(parent, j):
    if parent[j] == -1:
        print(j, end=' ')
        return None
    route(parent, parent[j])
    print(j, end=' ')


def path(costs, parents, src=0):
    print("Node \tdistance from Source \tPath from source node")
    for i in range(0, len(costs)):
        print(f"\n{src} \t => \t\t\t{costs[i]}\t\t\t\t", end='')
        route(parents, i)
        print()


s = int(input("enter start point, please: \n"))
result = alg_dik(gh, s)
print(f"cost from {s}-node to other nodes: {result}. Zero for start node.")


