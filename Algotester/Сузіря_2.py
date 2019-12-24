def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path
# N - Amount of vertex
# M - Amount of edges
N, M = map(int, input().split())

G = {key : list() for key in range(1,N + 1)} # Graph generator

# for i in range(N-1):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)


#G = [set() for _ in range(1, N+1)]
# add edges
#print(G)
links = {key : set() for key in range(1,N + 1)} # Graph generator
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    links[a].add(b)

# print(G)
# print(links)
used = set()
#
# #print(G)
# #print(vkazivniki)
stars = []
for i in G:
    counter = 0
    history = set()
    if i not in used:
        history = dfs_iterative(G, i)
        #print(history)
        for j in history:
            used.add(j)

        for i in history:
            counter += len(links[i])
        stars.append(counter)

print(len(stars))
stars.sort()
for i in stars:
    print(i)

