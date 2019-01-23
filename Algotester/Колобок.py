import collections
counter = collections.Counter()

s = list(input().split())
s = [x.lower() for x in s]

for word in s:
    counter[word] += 1

print(len(counter))