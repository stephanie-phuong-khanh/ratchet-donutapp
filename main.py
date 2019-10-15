#!/usr/bin/python3

import sys
import random
import copy

name_file = sys.argv[1]

with open(name_file,'r') as n:
    names = n.readlines()
names = [l.rstrip() for l in names]

# round robin scheduling algorithm, producing n-1 rounds of pairings for n names
# TODO: support for odd number of members

rounds = []
for i in range(len(names)-1):
    week = []
    left = 0
    right = len(names)-1
    while (left < right):
        week.append([names[left], names[right]])
        left +=1
        right -=1
    rounds.append(week)

    # rotation: first name fixed while rest rotate clockwise
    index = len(names)-1
    temp = names[index]
    while (index > 1):
        names[index] = names[index-1]
        index -= 1
    names[1] = temp

# shuffle pairings to mimic randomness
random.shuffle(rounds)
for index, val in enumerate(rounds):
    print("--- WEEK " + str(index+1) + " ---")
    for pair in val:
        print(pair[0] + " - " + pair[1])
    print("\n")