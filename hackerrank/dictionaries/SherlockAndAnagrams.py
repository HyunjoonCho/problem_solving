import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    anagramCountDict = {}
    
    for substringLen in range(1, len(s)):
        for idx in range(len(s) + 1 - substringLen):
            key = ''.join(sorted(list(s[idx:idx + substringLen])))
            if key in anagramCountDict.keys():
                anagramCountDict[key] += 1
            else: 
                anagramCountDict[key] = 1

    anagramCount = 0
    for val in list(anagramCountDict.values()):
        anagramCount += val * (val - 1) / 2

    return int(anagramCount)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(str(result))
