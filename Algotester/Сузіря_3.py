N, M = input().split()
N = int(N)
M = int(M)

nums = []
for i in range(M):
    nums.append(list(map(int, input().split())))

cons = [[{nums[0][0], nums[0][1]}, 1]]

for i in range(1, M):
    for j in range(len(cons)):
        if nums[i][0] in cons[j][0] or nums[i][1] in cons[j][0]:
            cons[j][1] += 1
            cons[j][0].update(nums[i])
            print(cons)
            break
        if j == len(cons)-1:
            cons.append([{nums[i][0], nums[i][1]}, 1])
            print(cons)

allStars = set()
for i in range(len(cons)):
    allStars.update(cons[i][0])

consNum = len(cons)
singleStars = 0
if len(allStars) < N:
    singleStars = N - len(allStars)
    consNum += singleStars

print(consNum)
print(allStars)
print("allStars:" + str(len(allStars)))

conects = []
for i in range(len(cons)):
    conects.append(cons[i][1])

conects.sort()


for i in range(singleStars):
    print(0)

for i in conects:
    print(i)