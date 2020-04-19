#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0 
    pos = 0 
    size = len(c)
    while pos <= size - 2: # possility of pos reaching c[-2]
            if pos == size - 2:
                jump = jump + 1
                break
            if c[pos+2] == 0:
                pos = pos + 2
            elif c[pos+1] == 0:
                pos = pos + 1
            jump = jump + 1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
