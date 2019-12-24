N = int(input())
G = {key : set() for key in range(N+1)}

def dfs(vertex, used, history):
    used.add(vertex)
    history.add(vertex)
    for neib in G[vertex]:
        if neib not in used:
            dfs(neib, used, history)

for i in range(N - 1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    G[a].add(b)
    G[b].add(a)


used = set()
visited = []
counter = 0
for i in G:
    #print(i)
    #print(used)
    if i not in used:
        history = set()
        dfs(i, used, history)
        if len(history) > 1:
            counter += 1
        visited.append(len(history))

print(len(visited) - 2)
