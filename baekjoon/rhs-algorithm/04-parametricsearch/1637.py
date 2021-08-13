from sys import stdin

N = int(stdin.readline())

nums = []
totalCount = 0

l = 2 ** 31 - 1
r = 0

for _ in range(N):
    A, C, B = map(int, stdin.readline().split())
    if l > A:
        l = A
    if C > r:
        r = C
    nums.append((A, C, B))
    totalCount += ((C - A) // B  + 1) & 1
nums.sort()

def rangeCount(upperBound):
    count = 0
    for i in range(N):
        if nums[i][0] > upperBound:
            break
        count += (min(nums[i][1], upperBound) - nums[i][0]) // nums[i][2] + 1
    return count


if totalCount % 2 == 0:
    print('NOTHING')
else:
    while l <= r:
        m = (l + r) // 2
        count = rangeCount(m) - rangeCount(l - 1)
        if count % 2 == 0:
            l = m + 1
        else:
            res = m
            r = m - 1

    print(res, rangeCount(res) - rangeCount(res - 1))