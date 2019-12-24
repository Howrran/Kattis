import sys
sys.setrecursionlimit(100000)

def dfs(vertex, used, history):
    global counter

    used.add(vertex)
    history.add(vertex)
    if len(links[vertex]) == 0:
        if G[vertex] > 0:
            counter += G[vertex]

        # print('We are in ', vertex)
        # print('counter = ', counter)
    else:
        for neib in links[vertex]:
            if neib not in used:
                dfs(neib, used, history)


# N - Amount of vertex
# M - Amount of edges
N, M = map(int, input().split())

G = dict()# Graph generator
#G = [set() for _ in range(1, N+1)]
# add edges
#print(G)
links = {key : set() for key in range(1,N + 1)} # Graph generator
for i in range(1, N + 1):
    a, b = map(int, input().split())
    G[i] = a - b

for i in range(1, M + 1):
    a, b = map(int, input().split())
    links[a].add(b)
    links[b].add(a)

#print(G)
#print(links)

used = set()

counter = 0
for i in G:
    history = set()
    dfs(i, used, history)
    c = 0
    #print(history)
    if len(history) > 1:
        for i in history:
            c += G[i]
        if c > 0:
            counter += c
            #print('counter links + = ',c)

print(counter)



