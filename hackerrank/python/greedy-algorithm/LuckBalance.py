#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    importantContests = []
    for i in range(k):
        importantContests.append(0)

    summedLuck = 0
    for luck, importance in contests:
        if not importance:
            summedLuck += luck
        elif k > 0 and luck > importantContests[0]: 
                summedLuck -= importantContests[0]
                i = 1
                while i < k and luck > importantContests[i]:
                    importantContests[i - 1] = importantContests[i]
                    i += 1
                importantContests[i - 1] = luck
        else:
            summedLuck -= luck
    summedLuck += sum(importantContests)

    return summedLuck

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')