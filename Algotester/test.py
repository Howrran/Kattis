s = sorted(input())

if len(s) and s[0] == '0':
    counter = 0
    for i in s:
        if i == '0':
            counter +=1
        else:
            break
        s[0],s[counter] = s[counter], s[0]

print(''.join(s), ''.join(sorted(s,reverse=True)))