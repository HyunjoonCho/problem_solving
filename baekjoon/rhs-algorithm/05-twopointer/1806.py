from sys import stdin

N, S = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

l = 0
r = 0
currentSum = 0
minLen = N + 1

while r < N:
    currentSum += seq[r]
    r += 1
    if currentSum >= S:
        while l < r:
            currentSum -= seq[l]
            l += 1
            if currentSum < S:
                minLen = r - l + 1 if r - l + 1 < minLen else minLen
                break
if minLen == N + 1:
    minLen = 0
print(minLen)
