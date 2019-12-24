# функція, яка визначає чи можемо ми розрізати краватки довжиною length на M депутатів
# рахує для скількох депутатів можемо розрізати краватки такою довжиною
def f(length):
    s = 0
    for i in range(N):
        s += int(kravatki[i] / length)

    if s >= M:
        return 1
    else:
        return 0

# N - к-сть краваток, M - к-сть депутатів
N, M = map(int, input().split())

kravatki = list(map(int, input().split()))

a = max(kravatki) / M
b = max(kravatki) + 1
c = 0

while b - a >= 0.0001:
    c = (a + b) / 2
    if f(c):
        a = c
    else:
        b = c

print("{0:.8f}".format(c))