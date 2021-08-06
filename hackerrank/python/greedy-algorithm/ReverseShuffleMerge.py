import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    # Write your code here
    letterCount = []
    for i in range(26):
        letterCount.append(0)
    
    currentCount = list(letterCount) # empty

    base = ord('a')
    for c in s:
        letterCount[ord(c) - base] += 1

    remainingCount = list(letterCount) # same as letter count
    halvedCount = [x//2 for x in letterCount]

    currentSubsequence = []

    for c in [ord(char) - base for char in reversed(s)]:
        if currentCount[c] < halvedCount[c]:
            while (currentSubsequence and currentSubsequence[-1] > c and 
                currentCount[currentSubsequence[-1]] + remainingCount[currentSubsequence[-1]] > halvedCount[currentSubsequence[-1]]):
                poppedChar = currentSubsequence.pop()
                currentCount[poppedChar] -= 1
            currentSubsequence.append(c)
            currentCount[c] += 1
        remainingCount[c] -= 1

    return ''.join([chr(c + base) for c in currentSubsequence])

if __name__ == '__main__':
    s = input()

    result = reverseShuffleMerge(s)

    print(result + '\n')
