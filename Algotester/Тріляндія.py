from collections import deque

def bfs(start, goal, graph):
    visited, queue = set([start]), deque([(start, 0)])
    while queue: # поки черга не пуста
        vertex, dist = queue.popleft() # дістаємо перший елемент з черги

        if vertex == goal: # якщо це наша ціль, пишемо відстань і виходимо
            print(dist)
            exit()

        for to in graph[vertex]: # проходимось по сусідам
            if to not in visited: # якщо сусід не відвіданий добавляємо його в чергу і в відвідані
                visited.add(to)
                queue.append((to, dist + 1))


N = int(input()) # вводимо к-сть секторів
start, finish = map(int, input().split())  # вводимо початковий та кінцевий сектор

vertices = {} #словник з вершинами
edges = {} # словник з ребрами


for i in range(1, N + 1):
    x1, y1, z1 = (map(float, input().split())) # вводимо координати точок
    f1 = (x1, y1, z1) # зберігаємо точку
    x2, y2, z2 = (map(float, input().split()))
    f2 = (x2, y2, z2)
    x3, y3, z3 = (map(float, input().split()))
    f3 = (x3, y3, z3)
    p = (f1, f2, f3) # зберігаємо зону

    vertices[i] = set()
    #
    # тут корочи ми утворюємо ребра)))))
    # тіпу зона і зєднана такимим ребрами
    #
    for e in p:
        for x in p:
            if e == x:
                continue
            vertices[i].add(tuple(sorted([e, x])))


    #
    # А тута кароче ми записуємо яке ребро зєднане з якими зонами
    # edge =  ((0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    # edges[edge] =  {1, 3}
    # по типу то ребро зєднує 1 і 3 зони
    for edge in vertices[i]:
        if edge not in edges:
            edges[edge] = set()
        edges[edge].add(i)

graph = {}

#
# тут ми утворюємо граф)))
# граф тримає в собі
# {1: {1, 3}, 2: {2, 4}, 3: {1, 3, 4}, 4: {2, 3, 4}}
# зона 1 зєднана з 1 і 3(хотя це трохи тупо но лан)
# думаю ти поняв))
for i in range(1, N + 1):
    graph[i] = set()
    for edge in vertices[i]:
        graph[i] |= edges[edge]

bfs(start, finish, graph)
print(-1)
