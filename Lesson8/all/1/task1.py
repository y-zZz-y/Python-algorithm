# Задание 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from collections import namedtuple

N = int(input('Введите количество друзей: '))
Vertex = namedtuple('Vertex', ['vertex1', 'vertex2'])
graph = []

for i in range(0, N):
    for j in range(i + 1, N):
        graph.append([Vertex(i, j)])

#print(*graph, sep='\n')
print(f'Количество рукопожатий: {len(graph)}')