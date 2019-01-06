#!/usr/bin/python3.7
from time import time
ts = []
iterations=datasetMult=1
printAns=True
for _ in range(iterations):
    t0 = time()
    import re
    import numpy as np
    events = sorted(list(filter(lambda x: x!='', open("inputs/4.txt").read().split("\n")*datasetMult)))
    shifts = []

    for i, j in enumerate(events):
        if "Guard" in j and i!=0:
            currentShiftLen = 1
            shifts.append(currentShift)
            currentShift = [j]
        elif i==0:
            currentShift = [j]
        else:
            currentShift.append(j)

    guard = {}

    pattern = re.compile(r"#(\d{1,4})")
    timePattern = re.compile(r"\d{1,2}:(\d{1,2})")

    guardTotalSleep, guardSleepTimes = {},{}

    # parse the data in the file
    for shift in shifts:
        guardNum = int(pattern.search(shift[0]).groups()[0])
        if guardNum not in guardTotalSleep:
            guardSleepTimes[guardNum] = []
            guardTotalSleep[guardNum] = 0

        for i in zip(shift[1::2], shift[2::2]):
            # none of the guards fall asleep after 1am so we dont need to store the hour
            start, end = map(lambda t: int(timePattern.search(t).groups()[0]), i)
            guardTotalSleep[guardNum] += (end-start)
            guardSleepTimes[guardNum].append(range(start, end))

    # find the guard who is asleep the most
    maxSleep = max(guardTotalSleep.values())
    for guard in guardTotalSleep:
        if guardTotalSleep[guard] == maxSleep:
            maxSleepGuard = guard

    # find the time they are asleep for the most
    hour = np.zeros(60, dtype='uint8')
    for sleepRange in guardSleepTimes[maxSleepGuard]:
        hour[list(sleepRange)] += 1

    mostOftenAsleep = np.argmax(hour)

    t1 = time()
    if printAns:
        print(f"part 1: [{maxSleepGuard*mostOftenAsleep}]")
    t2 = time()
    # find the most minutes asleep of all the guards
    sleepiestGuardID = minutesAsleep = chosenMinute = 0
    for guard in guardSleepTimes:
        hour = np.zeros(60,dtype='uint8')
        for sleepRange in guardSleepTimes[guard]:
            hour[list(sleepRange)] += 1
        if max(hour)>minutesAsleep:
            sleepiestGuardID,minutesAsleep,chosenMinute = guard,max(hour),np.argmax(hour)

    print(f"part 2: [{chosenMinute*sleepiestGuardID}]")
    ts.append((time()-t0)-(t2-t1))
print(np.average(np.array(ts)))
