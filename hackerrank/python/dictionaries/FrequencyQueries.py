#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    numCount = defaultdict(lambda : 0)
    invertedIndex = defaultdict(lambda : 0)
    resultArr = []

    for query in queries:
        if query[0] == 1:
            decrementValue(invertedIndex, numCount[query[1]])
            incrementValue(numCount, query[1])
            incrementValue(invertedIndex, numCount[query[1]])
        elif query[0] == 2:
            decrementValue(invertedIndex, numCount[query[1]])
            decrementValue(numCount, query[1])
            incrementValue(invertedIndex, numCount[query[1]])
        else:
            if query[1] in invertedIndex and invertedIndex[query[1]] > 0:
                resultArr.append(1)
            else:
                resultArr.append(0)

    return resultArr

def incrementValue(map, key):
    map[key] += 1

def decrementValue(map, key):
    if map[key] > 0:
        map[key] -= 1

if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))