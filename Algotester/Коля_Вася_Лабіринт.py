import sys
sys.setrecursionlimit(100000)
start = 1
def find_parent(vertex, current, parents):
    global cycles
    global start
    # if vertex == start:
    #     return
    #print("Enter cycle find from {} to {}".format(current, vertex))
    #print('cycle = ', cycles)
    #print()
    #print(parents)
    #print()
    #print('!!!!!!!!!!!!!!!')

    path = [current]
    current = current
    c = 0
    while current != vertex:

        # if current == vertex:
        #     print("Current == vertex: {} = {}".format(current, vertex))

        #print('curent = ', current)
        #print('parents = ', parents[current])
        #print('vertex = ', vertex)
        next_current = parents[current]
        if next_current == current or next_current == start:
            break
        current = next_current
        path.append(current)
    #     c += 1
    #     if c ==5:
    #         print(c)
    #         break
    # #print('FIND CYCLE')
    for i in path:
        cycles.append(i)

def dfs(vertex, used, parent):
    global cycles
    used.add(vertex)
    #print('We are in {}'.format(vertex))
    for neib in G[vertex]:
        if neib not in used:
            parent[neib] = vertex
            dfs(neib, used, parent)
        elif neib in used and neib != parent[vertex] and neib not in cycles:
            find_parent(neib, vertex, parent)


N = int(input())

G = {key :set() for key in range(1, N+1)}
parent = {}
cycles = []
used = set()

for _ in range(N):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)


dfs(1,used, parent)

#print('CYCLE:')
print(len(cycles))
for i in sorted(cycles):
    print(i, end=' ')
#print("used")
#print(used)