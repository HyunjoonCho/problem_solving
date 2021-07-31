import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    toyCount = 0
    while not prices:
        currentMin = prices[0]
        for price in prices:
            if price < currentMin:
                currentMin = price
        if k > currentMin:
            prices.remove(currentMin)
            k -= currentMin
            toyCount += 1
        else:
            break
    
    return toyCount

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')