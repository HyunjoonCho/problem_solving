from sys import stdin

N = int(stdin.readline())
seq = sorted(list(map(int, stdin.readline().split())))

def isGood(targetIdx):
    l = 0
    r = N - 1
    target = seq[targetIdx]
    while l < r:
        if l == targetIdx:
            l += 1
        if r == targetIdx:
            r -= 1
        if l >= r:
            break
        sum = seq[l] + seq[r]
        if sum == target:
            return True
        elif sum < target:
            l += 1
        else:
            r -= 1
    return False

count = 0
for i in range(N):
    if isGood(i):
        count += 1
print(count)