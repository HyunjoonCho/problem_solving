from sys import stdin

N, C = map(int, stdin.readline().split())
houseLocs = []
for _ in range(N):
    houseLocs.append(int(stdin.readline()))
houseLocs.sort()

def possibleCount(dist):
    currentLoc = houseLocs[0]
    count = 1
    for loc in houseLocs[1:]:
        if loc - currentLoc >= dist:
            count += 1
            currentLoc = loc

    return count

def binarySearch(l, r):
    if l > r:
        return r
    else:
        m = (l + r) // 2
        if possibleCount(m) >= C:
            return binarySearch(m + 1, r)
        else:
            return binarySearch(l, m - 1)

print(str(binarySearch(0, (houseLocs[-1] - houseLocs[0]) // (C - 1))))