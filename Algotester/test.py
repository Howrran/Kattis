d = {1 : 0, 2 : 0, 3 : 1}

d[1] += 1

m = -1
m_index = -1
for i in d:
    if d[i] > m:
        m = d[i]
        m_index = i

print(m, m_index)