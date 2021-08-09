#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    count, _ = mergeSort(arr)
    return count

def mergeSort(arr):
    if len(arr) == 1:
        return 0, arr
    else :
        firstCount, firstArr = mergeSort(arr[:len(arr)//2])
        secondCount, secondArr = mergeSort(arr[len(arr)//2:]) 
        count, mergedArr = merge(firstArr, secondArr)
        return firstCount + secondCount + count, mergedArr

def merge(firstArr, secondArr):
    mergedArr = []
    inversionCount = 0

    firstIdx = 0
    firstLen = len(firstArr)
    secondIdx = 0
    secondLen = len(secondArr)

    while firstIdx != firstLen or secondIdx != secondLen:
        if firstIdx == firstLen:
            mergedArr += secondArr[secondIdx:]
            secondIdx = secondLen
        elif secondIdx == secondLen:
            mergedArr += firstArr[firstIdx:]
            firstIdx = firstLen
        elif firstArr[firstIdx] <= secondArr[secondIdx]:
            mergedArr.append(firstArr[firstIdx])
            firstIdx += 1
        else:
            mergedArr.append(secondArr[secondIdx])
            secondIdx += 1
            inversionCount += firstLen - firstIdx
    return inversionCount, mergedArr

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result) + '\n')