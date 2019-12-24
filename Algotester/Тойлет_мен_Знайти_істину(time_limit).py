def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# N - Amount of vertex
# M - Amount of edges
N, M = map(int, input().split())

G = {key : set() for key in range(1,N + 1)} # Graph generator
#G = [set() for _ in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)

for i, j in enumerate(G):
    used = set()
    #dfs(j,used)
    used = bfs(G,j)
    #print(used)
    if len(used) == N:
        print('{}'.format(i+1))
        sys.exit()


else:
    print('-1')



