n = int(input())
sols = sorted(list(map(int, input().split())))

def binarySearch(l, r, target):
    if l > r:
        if l == len(sols):
            return r
        elif r == -1 or sols[r] == target:
            return l
        elif abs(sols[l] + target) >= abs(sols[r] + target):
            return r
        else:
            return l
    else:
        m = (l + r)//2
        if sols[m] + target == 0:
            return m
        elif sols[m] + target > 0:
            return binarySearch(l, m - 1, target)
        else:
            return binarySearch(m + 1, r,  target)

upperBound = n - 1
minSum = 2 * 10**10
minPair = 0, 0
for i in range(n):
    if i < upperBound:
        idx = binarySearch(i + 1, upperBound, sols[i])
        if sols[i] + sols[idx] == 0:
            print(' '.join([str(sols[i]), str(sols[idx])]))
            break
        elif abs(sols[i] + sols[idx]) < minSum:
            minSum = abs(sols[i] + sols[idx])
            minPair = sols[i], sols[idx]
            upperBound = idx
    else:
        print(' '.join([str(minPair[0]), str(minPair[1])]))

# Reference solution; sort by its absolute value then only care about neighboring pair!