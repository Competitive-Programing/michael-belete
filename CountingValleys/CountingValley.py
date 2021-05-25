#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    previousLevel = None
    now = path[0]
    currentLevel = 1 if now == "U" else -1
    valleys = 0
    for i in range(1, len(path)):
        previousLevel = currentLevel
        now = path[i]
        currentLevel = currentLevel + 1 if now == "U" else currentLevel - 1
        if previousLevel < 0 and currentLevel == 0:
            valleys = valleys + 1
    return valleys 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
