from math import sqrt, pi, exp

import random

class Particle:
    def __init__(self,x,y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __str__(self):
        return f'{self.x}, {self.y}, {self.weight}'

def f(u):
    return ((1 / sqrt(2 * pi * o**2 )) * exp(-(u - u0)**2 / o**2))

particles = []

G = 100

N = int(input())
map = list(map(int, input().split()))
print(map)
#map = [(0,0),(5,0), (5,5), (0,5)]

M, K = map(int, input().split())

SL, Sx, Sy = map(int, input().split())

num = input()

if int(num[0]) == 1:
    x_start = int(num[2])
    y_start = int(num[4])

for i in range(G):
    p = Particle(random.randint(0, 5), random.randint(0, 5), 1/G)
    particles.append(p)

