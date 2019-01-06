#!/usr/bin/python3.7
from functools import reduce
from operator import add
from string import ascii_uppercase
from time import time
t0 = time()
pairs = {i:[] for i in ascii_uppercase}

for i in open("inputs/7.txt").read().split("\n")[:-1]:
    before, after = i[5], i[36]
    pairs[after].append(before)

# pairs relates a step to all the steps that must come before it

# first: find all the steps which require no others and execute them in alphabetic order
# checking each time that a new stel which is lower in the alphabet hasnt been opened up.

ans = ""
while len(ans) != 26:
    available = sorted([i for i in pairs if set(pairs[i]).issubset(set(ans)) and i not in ans])
    ans += available[0]

def checkAns(answer):
    for i in open("inputs/7.txt").read().split("\n")[:-1]:
        before, after = i[5], i[36]
        if answer.find(before) > answer.find(after):
            return False
    return True

if checkAns(ans):
    print(f"part 1: [{ans}] :: {time()-t0:.5f} seconds")
else:
    print("fail")
    exit()

def stepVal(step):
    return 1 + ascii_uppercase.find(step)

t1 = time()
secondsElapsed = 0
jobs = []
completed = ""
while len(completed) != 26:
    updatedJobs = []
    for job in jobs:
        step, timeLeft = job
        if timeLeft != 1:
            updatedJobs.append((step,timeLeft-1))
        else:
            completed += step
    secondsElapsed += 1
    jobs = updatedJobs
    available = sorted([i for i in pairs if set(pairs[i]).issubset(set(completed)) and i not in (set(completed)|set([job[0] for job in jobs]))])
    while available and len(jobs)<=5:
        newJob = available[0]
        jobs.append((newJob, 60+stepVal(newJob)))
        available = sorted([i for i in pairs if set(pairs[i]).issubset(set(completed)) and i not in (set(completed)|set([job[0] for job in jobs]))])

if checkAns(completed):
    print(f"part 2: [{secondsElapsed}] :: {time()-t1:.5f} seconds")
else:
    print("fail")
