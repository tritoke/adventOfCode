#!/usr/bin/python3.7
from itertools import product
import numpy as np
from operator import add, itemgetter
from functools import reduce
from time import time

serialNum = int(open("inputs/11.txt").read())

fuelCells = np.zeros((300, 300),dtype='int8')

# generate the fuelcells
for x,y in product(range(300), repeat=2):
    rackID = x+10
    powerLevel = rackID * y
    powerLevel += serialNum
    powerLevel *= rackID
    powerLevel = int(f"{powerLevel:03d}"[-3])
    powerLevel -= 5
    fuelCells[x,y] = powerLevel

def maxForBoxSize(boxSize):
    scores = np.zeros((300-boxSize,300-boxSize),dtype='int16')
    for i,j in product(range(300-boxSize), repeat=2):
        scores[i,j] = np.sum(fuelCells[i:i+boxSize,j:j+boxSize])

    index = np.unravel_index(np.argmax(scores, axis=None), scores.shape)
    return (scores[index], (*index,boxSize))
t0 = time()
print(f"part 1: [{maxForBoxSize(3)[1][:2]}] :: {time()-t0:.5f} seconds")
t1 = time()
print(f"part 2: [{max(map(maxForBoxSize, range(1,20)), key=itemgetter(0))[1]}] :: {time()-t1:.5f} seconds")
