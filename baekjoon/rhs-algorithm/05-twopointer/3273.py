import sys

rl = sys.stdin.readline

N = int(rl())
seq = sorted(list(map(int, rl().split())))
x = int(rl())

l = 0
r = N - 1

count = 0
while l < r:
    sum = seq[l] + seq[r]
    if sum == x:
        count += 1
        l += 1
        r -= 1
    elif sum < x:
        l += 1
    else:
        r -= 1
print(count)