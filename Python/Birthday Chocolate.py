#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    size = len(s)

    if m > size or sum(s) < d:
        return 0
    
    if m == size and sum(s) == d:
        return 1

    for i in range(0,size):
        added = s[i] + sum(s[i+1:i+m])
        if added == d:
            count += 1
    
    return count
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
