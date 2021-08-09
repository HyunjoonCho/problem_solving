import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    totalCount = 0
    prevChar = s[0]
    consecutiveCharCount = 0
    for i in range(n):
        if s[i] == prevChar:
            consecutiveCharCount += 1
        else:
            totalCount += consecutiveCharCount * (consecutiveCharCount + 1) // 2
            consecutiveCharCount = 1
            j = 1
            while i - j >= 0 and i + j < n:
                if s[i - j] == prevChar and s[i + j] == prevChar:
                    totalCount += 1
                    j += 1
                else:
                    break
        prevChar = s[i]
    totalCount += consecutiveCharCount * (consecutiveCharCount + 1) // 2

    return totalCount

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(str(result) + '\n')
