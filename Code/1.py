#!/usr/bin/python3.7
from time import time
t0 = time()
nums = list(map(int, filter(lambda x: x!="", open("inputs/1.txt").read().split("\n"))))
print(f"part 1: [{sum(nums)}] :: {time()-t0:.5f} seconds")

t1=time()
from itertools import cycle
total = 0
totals = set()
cycleNums = cycle(nums)
while True:
    current = next(cycleNums)
    total += current
    if total in totals:
        print(f"part 2: [{total}] :: {time()-t0:.5f} seconds")
        break
    totals.update([total])
