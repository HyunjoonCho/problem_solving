N, M = map(int, input().split())
heights = list(map(int, input().split()))

def sumHeights(cutH):
    return sum([height - cutH for height in heights if height > cutH])

def binarySearch(l, r):
    if l > r:
        return r
    else:
        m = (l + r) // 2
        sum = sumHeights(m)
        if sum == M:
            return m
        elif sum > M:
            return binarySearch(m + 1, r)
        else:
            return binarySearch(l, m - 1)

print(str(binarySearch(0, 10**9)))