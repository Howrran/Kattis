import sys
sys.setrecursionlimit(100000)

def dfs(vertex, used, history):
    used.add(vertex)
    history.add(vertex)
    for neib in G[vertex]:
        if neib not in used:
            dfs(neib, used, history)

# N - Amount of vertex
# M - Amount of edges
N, M = map(int, input().split())

G = {key : list() for key in range(1,N + 1)} # Graph generator
#G = [set() for _ in range(1, N+1)]
# add edges
#print(G)
links = {key : list() for key in range(1,N + 1)} # Graph generator
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    G[a].append(b)
    G[b].append(a)
    links[a].append(b)

# print(G)
# print(links)
used = set()

#print(G)
#print(vkazivniki)
stars = []
for i in G:
    counter = 0
    history = set()
    if i not in used:
        dfs(i, used, history)
        for i in history:
            counter += len(links[i])
        stars.append(counter)

print(len(stars))
stars.sort()
for i in stars:
    print(i)


