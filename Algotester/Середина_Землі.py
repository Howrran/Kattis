from math import sqrt
e = 0.00000001
def func(x,y):
    sum = 0
    for i in range(n):
        sum += sqrt ((points[i][0] - x)**2 + (points[i][1] - y)**2)
    return sum

def fx(x,y, step):
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(n):
        sum1 += -(points[i][0] - x)/sqrt((points[i][0] - x)**2 + (points[i][1] - y)**2)
        sum2 += -(points[i][1] - y) / sqrt((points[i][0] - x) ** 2 + (points[i][1] - y) ** 2)
        sum3 += sqrt((points[i][0] - x) ** 2 + (points[i][1] - y) ** 2)
    return ((sum1 * step), (sum2 * step), (sum3))

def fy(x,y,step):
    sum = 0
    for i in range(n):
        sum += -(points[i][1] - y) / sqrt((points[i][0] - x) ** 2 + (points[i][1] - y) ** 2)

    return sum * step


step = 1
n = int(input())

points = []

for i in range(n):
    x,y = map(int, input().split())
    points.append((x,y))

x = 2
y = 2
prev, cur = 99999,9999

while True:
    if prev <= cur:
        step /= 10
    if step < e:
        break

    prev = cur
    xs, ys, cur = fx(x, y, step)
    x -= step * xs
    y -= step * ys




# print(x,y)
# print(func(x,y))
print(cur)
