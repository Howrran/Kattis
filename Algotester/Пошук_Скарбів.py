import sys
sys.setrecursionlimit(100000)
def dfs(vertex, used, hours):
    global counter
    counter += 1 # add counter when we enter the vertex
    hours.add(counter)
    #print('Vertex = {}, cntr = {}'.format(vertex, counter))
    used.add(vertex)
    # дивимось на суміжні вершини, якщо є не відвідана йдемо до неї
    for neib in G[vertex]:
        if neib not in used:
            #print(neib)
            dfs(neib, used, hours)
    counter += 1 # add counter when we leave the vertex

N = int(input()) # vertex amount
#G = {key : set() for key in range(1,N + 1)} # Graph generator
G = [set() for _ in range(N+1)]
# add edges
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
used = set()
hours = set()

#print(G)

counter = -1
dfs(1,used, hours)

#M = (1/N) * sum(hours)
#print(M * N)
#print(hours)
print(sum(hours))
