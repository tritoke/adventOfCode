#!/usr/bin/python3.7
from PIL import Image
import numpy as np
from functools import reduce
from operator import add
from time import time

t0 = time()

coords =  list(map(lambda x: tuple(map(int, x.split(", "))),filter(lambda x: x!="", open("inputs/6.txt").read().split("\n"))))

area = np.zeros((400,400), dtype = 'uint32')
points = np.array(coords)

pointNums = {}
for i, j in enumerate(points):
    pointNums[coords[i]] = i+1

def closestPoint(point):
    def manhattenDistance(coord):
        a,b = point
        c,d = coord
        return abs(a-c)+abs(b-d)

    distances = list(map(manhattenDistance, coords))
    minimum = min(distances)
    if distances.count(minimum) > 1:
        return 0
    else:
        for coord in coords:
            if manhattenDistance(coord) == minimum:
                #print(minimum, coord)
                return pointNums[coord]

for i,j in reduce(add, [[(x,y) for x in range(400)] for y in range(400)]):
    area[i,j] = closestPoint((i,j))

edgePoints = set(area[0]) | set(area[-1]) | set(area[:,0]) | set(area[:,-1])

print(f"part 1: [{max([np.count_nonzero(area==i) for i in range(1,51) if i not in edgePoints])}] :: {time()-t0:.5f} seconds")

t1 = time()

for i, j in enumerate(points):
    area[j[0],j[1]] = 2**16-1

Image.fromarray(area*3, 'I').show()
total = 0
for i,j in reduce(add, [[(x,y) for x in range(400)] for y in range(400)]):
    if sum(abs(i-x)+abs(j-y) for x,y in coords) < 10000:
        total += 1
print(f"part 2: [{total}] :: {time()-t1:.5f} seconds")
