#!/usr/bin/python3.7
from time import time
from string import ascii_lowercase as letters
polymer = open("inputs/5.txt").read().strip()

def reactPolymer(x):
    stack = []
    for i in x:
        if stack and stack[-1].swapcase() == i:
            stack.pop()
        else:
            stack.append(i)
    return stack

t0 = time()
reacted = reactPolymer(polymer)
print(f"part 1: [{len(reacted)}] :: {time()-t0:.5f} seconds")

t1 = time()
reactedString = "".join(reacted)
print(f"part 2: [{min(map(lambda i:len(reactPolymer(reactedString.translate(str.maketrans({i:None,i.upper():None})))), letters))}] :: {time()-t1:.5f} seconds")
