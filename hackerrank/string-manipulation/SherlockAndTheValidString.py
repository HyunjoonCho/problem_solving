import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    charCount = []
    for i in range(26):
        charCount.append(0)
    
    base = ord('a')
    for c in list(s):
        charCount[ord(c) - base] += 1
    
    actualCount = [x for x in charCount if x != 0]
    if len(actualCount) == 1:
        return 'YES'
    if len(actualCount) == 2:
        if 1 in actualCount or abs(actualCount[0] - actualCount[1]) < 2:
            return 'YES'
        else:
            return 'NO'
    else:
        if actualCount[0] == actualCount[1]:
            expected = actualCount[0]
        elif actualCount[0] == actualCount[2]:
            expected = actualCount[0]
        elif actualCount[1] == actualCount[2]:
            expected = actualCount[1]
        else:
            return 'NO'
        oneCount = 0
        diffCount = 0
        for count in actualCount:
            if count == 1:
                oneCount += 1
            elif count == expected + 1:
                diffCount += 1
            elif count != expected:
                return 'NO'
        if oneCount + diffCount > 1:
            return 'NO'
        else:
            return 'YES'

if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result + '\n')
