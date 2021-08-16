import sys
rl = sys.stdin.readline

from collections import defaultdict
countNum = defaultdict(int)

N = int(rl())
seq = list(map(int, rl().split()))

count = 0
countSubs = lambda x, y: (x - y + 1) * (x - y) // 2

l = 0
r = 0
while l < N:
    if r == N:
        count += countSubs(r, l)
        break
    if not countNum[seq[r]]:
        countNum[seq[r]] += 1
        r += 1
    else:
        count += countSubs(r, l)
        countNum[seq[r]] += 1
        while countNum[seq[r]] != 1:
            countNum[seq[l]] -= 1
            l += 1
        count -= countSubs(r, l)
        r += 1
print(count)

# Look at sol, way more simple! starting from l, till r - count = r - l + 1! 