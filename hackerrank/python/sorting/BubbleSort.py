import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swapCount = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                swapCount += 1

    firstElem = a[0]
    lastElem = a[0]
    for elem in a:
        if elem < firstElem:
            firstElem = elem
        if elem > lastElem:
            lastElem = elem

    print(f'Array is sorted in {swapCount} swaps.\nFirst Element: {firstElem}\nLast Element: {lastElem}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
