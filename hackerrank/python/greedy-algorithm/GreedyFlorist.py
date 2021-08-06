import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    mult = 0
    currentCount = 0
    totalCost = 0
    for price in reversed(sorted(c)):
        if currentCount % k == 0:
            mult += 1
        totalCost += price * mult
        currentCount += 1
        
    return totalCost

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(str(minimumCost) + '\n')