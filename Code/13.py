#!/usr/bin/python3
import numpy as np
from functools import reduce
from operator import add

carts = set("<^v>")

initialState = np.array(open("inputs/13.txt").read().split("\n")[:-2])

a = np.ravel(list(map(lambda x: np.where(x in carts), initialState)))
print(a)

