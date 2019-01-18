C = float(input())
L = int(input())

cost = 0.0
for i in range(L):
    w,l = map(float,input().split(' '))
    cost += C * w * l

print('{0:.7f}'.format(cost))