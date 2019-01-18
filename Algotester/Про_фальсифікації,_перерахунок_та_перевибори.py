import math
n,s = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

for i in range(n):
    s -= math.fabs(arr1[i] - arr2[i])
    
print(int(s))