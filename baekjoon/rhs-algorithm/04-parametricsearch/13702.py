from sys import stdin

N, K = map(int, stdin.readline().split())
mLiters = []
for _ in range(N):
    mLiters.append(int(stdin.readline()))

l = 0
r = max(mLiters)

res = l
while l <= r:
    m = (l + r) // 2
    pplCount = sum([ml // m for ml in mLiters])
    if pplCount < K:
        r = m - 1
    else:
        res = m
        l = m + 1
print(res)