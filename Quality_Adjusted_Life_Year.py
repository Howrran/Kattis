N = int(input())

QALY = 0
for i in range(N):
    q,y = map(float,input().split(" "))
    QALY += q*y

print('{0:.3f}'.format(QALY))