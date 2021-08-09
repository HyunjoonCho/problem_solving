import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    table = [0 for _ in range(len(s1) + 1)]
    for i in range(len(s2)):
        s2Char = s2[i]
        prevDiagonalVal = 0
        for j in range(1, len(s1) + 1):
            temp = prevDiagonalVal + 1
            prevDiagonalVal = table[j]
            if s1[j - 1] == s2Char:
                table[j] = temp
            else:
                table[j] = max(table[j - 1], table[j])
    return table[len(s1)]

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(str(result) + '\n')
