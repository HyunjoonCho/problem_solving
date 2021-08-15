from sys import stdin

N, M = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

l = r = 0
currentSum = 0
count = 0
while r < N:
    currentSum += seq[r]
    r += 1
    if currentSum == M:
        count += 1
    elif currentSum > M:
        while l < r:
            currentSum -= seq[l]
            l += 1
            if currentSum <= M:
                if currentSum == M:
                    count += 1
                break

print(count)