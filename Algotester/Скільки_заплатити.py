a,b = map(int,input().split())
if b < a:
    a,b = b,a
if b - a <= 1:
    print(-1)
else:
    print(a+1)