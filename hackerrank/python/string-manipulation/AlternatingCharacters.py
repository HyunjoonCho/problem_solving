import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    count = 0
    isA = s[0] == 'A'
    for i in range(1, len(s)):
        if (isA and s[i] == 'A') or (not isA and s[i] == 'B'):
            count += 1
        else:
            isA = not isA

    return count

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')
