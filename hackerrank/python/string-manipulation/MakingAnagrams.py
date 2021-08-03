import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    countA = []
    countB = []

    for i in range(26):
        countA.append(0)
        countB.append(0)
    
    base = ord('a')
    for c in list(a):
        countA[ord(c) - base] += 1
    for c in list(b):
        countB[ord(c) - base] += 1
    
    count = 0
    for i in range(26):
        if countA[i] >= countB[i]:
            count += countA[i] - countB[i]
        else:
            count += countB[i] - countA[i]
    
    return count

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')