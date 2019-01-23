import time
def foo(n):
    # n = input()
    time.sleep(1)
    s = ''.join(sorted(n))

    if len(s) > 1 and s[0] == '0':
        ss = list(s)
        counter = 0
        while (ss[counter] == '0'):
            counter += 1
        ss[0], ss[counter] = ss[counter], ss[0]
        s = ''.join(ss)

    min = s
    max = ''.join(sorted(n, reverse=True))

    print('{} {}'.format(min, max))
    if max < min:
        print('PZDCNAXYIBLED')
        time.sleep(5)




count = 1000
while count < 10000000:
    foo(str(count))
    count += 1
