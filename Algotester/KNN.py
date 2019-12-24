class Postcard:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

def get_distance(object1, object2):
    dist = max(abs(object1.weight - object2.weight),
               abs(object1.height - object2.height))
    return (dist, object2.clas)

def find_clas(neighbors):
    max_element, index = -1, -1
    for i in neighbors:
        if i[0] > max_element:
            max_element = i[0]
            index = i[1]
    return index

# N - amount of classes
# K - k nearest neibhours
# M - amount of objects to classify
N, K, M = map(int, input().split())

cards = []
for i in range(1, N + 1):
    w, h = map(int, input().split())
    p = Postcard(w,h)
    p.clas = i
    cards.append(p)

for i in range(M):
    w, h = map(int, input().split())
    object = Postcard(w, h)

    neighbors = []
    distances = {key: 0 for key in range(1, N + 1)}
    for neib in cards:
        distance = get_distance(object, neib)
        if len(neighbors) < K:
            neighbors.append(distance)
        else:
            neighbors.sort()
            if neighbors[-1][0] > distance[0]:
                neighbors[-1] = distance


    new_clas = find_clas(neighbors)
    object.clas = new_clas
    cards.append(object)

for i in cards[N:]:
    print(i.clas, end= ' ')