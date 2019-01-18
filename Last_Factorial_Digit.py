def fact(x):
    if x == 0:
        return 1

    return x * fact(x-1)

def last_num(x):
    num = str(x)
    return num[-1]


T = int(input())

arr = []

for i in range(T):
    i = int(input())
    arr.append(i)


for i in arr:
    i = fact(i)
    i = last_num(i)
    print(i)
