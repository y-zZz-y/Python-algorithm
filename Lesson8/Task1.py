# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
#
# Примечание. Решите задачу при помощи построения графа.

n = 6
graph = [] #Список смежности

i = 0
while i < n:
    graph.append([el for el in range(n-i,n)])
    i += 1


print(graph)
print(f'{sum([len(el) for el in graph])} рукопожатий')