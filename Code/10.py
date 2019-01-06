#!/usr/bin/python3.7
import re
import numpy as np
from PIL import Image
from time import time
from operator import itemgetter
lines = open("inputs/10.txt").read().split("\n")[:-1]
numPoints = len(lines)
pattern = re.compile(r"-?\d+")

t0 = time()
inputAsColumns = list(zip(*map(lambda x: map(int, pattern.findall(x)), lines)))
scores = []
def makeSky(secondsElapsed):
    xPos, yPos, xVel, yVel = map(lambda x: np.array(x, dtype='int32'), inputAsColumns)

    xPos += (secondsElapsed*xVel)
    yPos += (secondsElapsed*yVel)
    xPos -= np.amin(xPos)
    yPos -= np.amin(yPos)

    shape = (np.amax(xPos)+1, np.amax(yPos)+1)
    #print(i, shape)

    sky = np.zeros(shape, dtype='uint32')
    sky[xPos, yPos] += (2**16)-1
    return sky

for i in range(9750, 10250):
    scores.append(sum(map(np.count_nonzero, makeSky(i))))
timeToAlign = 9750 + min(enumerate(scores), key=itemgetter(1))[0]
Image.fromarray(makeSky(10009), 'I').show()
print(f"part 2: [{timeToAlign}] :: {time()-t0} seconds")
