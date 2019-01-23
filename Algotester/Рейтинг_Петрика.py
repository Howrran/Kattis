x,y,z = map(int,input().split())

if z < x - y:
    print('-1')
elif x + y < z:
    print(x+y)
elif x + y > z:
    print(z)