#!/usr/bin/python3.7
from time import time
t0 = time()
ids = list(filter(lambda x: x!="", open("inputs/2.txt").read().split("\n")))
n2, n3 = 0, 0
for id in ids:
    s = [id.count(i) for i in set(id)]
    n2 += (2 in s)
    n3 += (3 in s)
print(f"part 1: [{n2*n3}] :: {time()-t0:.5f} seconds")

t1=time()
from functools import partial
b = False
for id in ids:
    p = partial(zip, id)
    func = lambda x: sum(i!=j for i,j in p(x))
    for i in ids:
        #print(i, id, func(i))
        if func(i) == 1:
            print(f"part 2: [{''.join(x for x, j in zip(i, id) if x == j)}] :: {time()-t1:.5f} seconds")
            b = True
            break
    if b: break
