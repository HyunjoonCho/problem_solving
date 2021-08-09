import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr = sorted(arr)
    min = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < min:
            min = abs(arr[i] - arr[i + 1])
    return min

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
