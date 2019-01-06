#!/usr/bin/python3.7
from time import time
data = open("inputs/12.txt").read().split("\n")
initialState = data[0].split()[-1]
stateChanges = dict(map(lambda x: x.split(" => "), data[2:-1]))
leftPad = 3
currentState = leftPad*"." + initialState + "."*80

def doStateChange(current, stateMap):
    current = ".."+current+".."
    return "".join(map(lambda x: stateMap[current[x[0]:x[0]+5]], enumerate(current[:-4])))

def scoreState(state):
    return sum((i-leftPad)*(j=="#") for i,j in enumerate(state))

#print(f"  0: {currentState} {scoreState(currentState)}")
t0 = time()
for i in range(20):
    currentState = doStateChange(currentState, stateChanges)
 #   print(f"{i+1:>3}: {currentState} {scoreState(currentState)}")

print(f"part 1: [{scoreState(currentState)}] :: {time()-t0:.5f} seconds")
t1 = time()
currentState += "."*1000
prevDiff = 0
iterations = 20
totalIterations = 50000000000
while True:
    nextState = doStateChange(currentState, stateChanges)
    iterations += 1
    currentDiff = scoreState(nextState)-scoreState(currentState)
    nextDiff = scoreState(doStateChange(nextState, stateChanges)) - scoreState(nextState)
    if prevDiff == currentDiff == nextDiff:
        finalScore = scoreState(nextState)
        break
    prevDiff = currentDiff
    currentState = nextState
finalScore += (totalIterations - iterations)*(currentDiff)
print(f"part 2: [{finalScore}] :: {time()-t1:.5f} seconds")

