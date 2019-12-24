n = int(input())

stikers = []
zasmytivsa = 0

for sproba in range(n):
    sproba = int(input())
    if sproba == 1:
        stikers.append(1)
    elif sproba == 2:
        if not stikers:
            zasmytivsa += 1
        else:
            stikers.remove(1)

print(zasmytivsa)