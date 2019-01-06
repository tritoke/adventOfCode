#!/usr/bin/python3.7
import numpy as np
from time import time
from PIL import Image
from functools import reduce
from operator import add
import re

t0 = time()
shape = (1000,1000)
fabric = np.zeros(shape, dtype='uint32')

t = list(map(lambda x: (tuple(map(int, x[-2][:-1].split(","))),tuple(map(int, x[-1].split("x")))), map(lambda x: x.split(), filter(lambda x: x!="", open("inputs/3.txt").read().split("\n")))))
for ((x,y),(width,height)) in t:
    fabric[x:x+width, y:y+height] += 1

Image.fromarray(fabric*(10**2), 'I').show()

print(f"part 1: [{np.count_nonzero(fabric > 1)}] :: {time()-t0:.5f} seconds")

t1 = time()
one = np.array(1)
for i, ((x,y),(width,height)) in enumerate(t):
    if set(np.unique(fabric[x:x+width,y:y+height])) == set(np.unique(one)):
        print(f"part 2: [{i+1}] :: {time()-t1:.5f} seconds")


