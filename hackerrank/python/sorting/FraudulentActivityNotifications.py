import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    notiCount = 0
    trailingExps = []
    for i in range(201):
        trailingExps.append(0)

    for i in range(len(expenditure)):
        if i >= d:
            if expenditure[i] >= 2 * getMedian(trailingExps, d):
                notiCount += 1
            trailingExps[expenditure[i - d]] -= 1
        trailingExps[expenditure[i]] += 1
    return notiCount

def getMedian(trailingExps, d):
    isEven = (d % 2 == 0)
    d = d//2 + 1
    median = 0
    for currentExp in range(201):
        if d > trailingExps[currentExp]:
            d -= trailingExps[currentExp]
            if isEven and d == 1:
                median += currentExp
        else:
            median += currentExp
            if d == 1 and isEven:
                median /= 2
            return median

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')