k = int(input())

s = input()
count = 0
for i in range(len(s)):
    #print('-6',s[i-6: i],'0', s[i:i+6],'+6' ,s[i+6:i+12])
    if s[i:i+6] == 'TOILET':
        if s[i-6: i] == 'TOILET' or s[i+6:i+12] == 'TOILET':
            continue
        else:
            count += 1

if count >= k:
    print("YES")
else:
    print('NO')