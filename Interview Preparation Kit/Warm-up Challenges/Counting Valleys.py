#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    valley = 0
    
    for l in s:
        if l == 'D':
            sea_level = sea_level - 1                
        elif l == 'U':
            sea_level = sea_level + 1
            if sea_level == 0:                      # As we require only Valley Count
                valley = valley + 1 
                
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
