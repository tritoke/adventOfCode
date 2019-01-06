#!/usr/bin/python3.7
from time import time

t0 = time()

numbers = list(map(int,open("inputs/8.txt").read().split()))
test = list(map(int,"2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()))

root = 0
usingArr = numbers

def part1(index):
    children = int(usingArr[index])
    metaDataEntries = int(usingArr[index+1])
    metaDataSum = 0
    nextChildIndex = index + 2

    for i in range(children):
        nextChildIndex, metadataSum = part1(nextChildIndex)
        metaDataSum += metadataSum

    metaDataStart = nextChildIndex

    for i in range(metaDataEntries):
        metaDataSum += usingArr[metaDataStart+i]
        nextChildIndex += 1
    return nextChildIndex, metaDataSum

finalNode, metaDataSum = part1(root)
print(f"part 1: [{metaDataSum}] :: {time()-t0:.5f} seconds")

def part2(index):
    value = 0
    children = int(usingArr[index])
    metaDataEntries = int(usingArr[index+1])
    nextChildIndex = index + 2
    childrenVals = []
    for i in range(children):
        nextChildIndex, childValue = part2(nextChildIndex)
        childrenVals.append(childValue)

    metaDataStart = nextChildIndex
    nextChildIndex += metaDataEntries

    if children != 0:
        for i in range(metaDataEntries):
            childValIndex = usingArr[metaDataStart+i] - 1
            try:
                value += childrenVals[childValIndex]
            except IndexError:
                pass

    else:
        for i in range(metaDataEntries):
            metadata = usingArr[metaDataStart+i]
            value += metadata
    return nextChildIndex, value
t1 = time()
finalNode, rootVal = part2(root)
print(f"part 2: [{rootVal}] :: {time()-t1:.5f} seconds")
