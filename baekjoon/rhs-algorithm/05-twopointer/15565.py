from sys import stdin

N, K = map(int, stdin.readline().split())
dolls = list(map(lambda x : 2 - int(x), stdin.readline().split()))

l = 0
r = 0
rCount = 0
minLen = N + 1

while r < N:
    if dolls[r]:
        rCount += 1
    r += 1
    if rCount == K:
        while l < r:
            isRyan = dolls[l]
            l += 1
            if isRyan:
                rCount -= 1
                minLen = r - l + 1 if r - l + 1 < minLen else minLen
                break

if minLen == N + 1:
    minLen = -1
print(minLen)