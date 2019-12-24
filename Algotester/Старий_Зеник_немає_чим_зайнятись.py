import sys
sys.setrecursionlimit(100000)

def dfs(vertex, used, parent):
    global start
    used.add(vertex)
    for neib in G[vertex]:
        if neib == start and neib != parent[vertex]:
            print(start)
            sys.exit()
        elif neib not in used:
            parent[neib] = vertex
            dfs(neib, used, parent)

N, M = map(int, input().split())

G = {key :set() for key in range(1, N+1)}
parent = {}
cycles = []

for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

for i in range(1, N + 1):
    used = set()
    start = i
    dfs(i, used, parent)

print(-1)
