"""Lesson 08 task 1"""
"""1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). 
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа."""

people = 4

# v1 with matrix
def hansdshake_amt(qty):
    graph = [[1] * qty for _ in range(qty)]
    total = 0
    for i in range(len(graph)):
        graph[i][i] = 0
        total += sum(graph[i])
    total //= 2

    print(*graph, sep='\n')
    print(f"Amount of handshakes is {int(total)}")


hansdshake_amt(people)

#  v2 with lists
def hansdshake_amt_list(qty):
    graph = []
    total = 0
    for i in range(qty):
        graph.append([1 for i in range(qty - i - 1)])
        total += sum(graph[i])
    print(*graph, sep='\n')
    return total

result = hansdshake_amt_list(people)
print(f"Amount of handshakes is {result}")
