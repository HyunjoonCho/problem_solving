N = int(input())
k = int(input())

def checkPosition(target):
    prevCount = 0
    currCount = 0
    for i in range(1, N + 1):
        prevCount += min(target // i, N)
        if target % i == 0 and target // i <= N:
            currCount += 1
            prevCount -= 1
    return prevCount, prevCount + currCount

l = 0
r = min(10**9, N**2)

while l <= r:
    m = (l + r) // 2
    lowerBound, upperBound = checkPosition(m)
    if upperBound < k:
        l = m + 1
    elif k <= lowerBound:
        r = m - 1
    else:
        print(m)
        break