import collections, itertools
def get_loops(MN):
    network = {}
    for a,b in MN:
        network[a].add(b) if a in network else network.update({a:{b}})
        network[b].add(a) if b in network else network.update({b:{a}})
    chain = collections.OrderedDict()
    def __loop_iterator(node):
        if node not in chain:
            chain[node] = None
            next = network[node]
            while next:
                n = next.pop()
                network[n].remove(node)
                yield from __loop_iterator(n)
            chain.popitem()
        else: yield tuple(itertools.chain(itertools.takewhile(lambda x: x is not node, reversed(chain)), (node,)))
    for n in network: return list(__loop_iterator(n))

N = int(input())
ch = []
for _ in range(N):
    a, b = map(int, input().split())
    ch.append([a,b])

res = get_loops(ch)

for i in res:
    ans = list(i)
ans.sort()
print(len(ans))
for i in ans:
    print(i,end = ' ')

