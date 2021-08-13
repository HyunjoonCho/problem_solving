from sys import stdin

N, M = map(int, stdin.readline().split())

dailyExps = []
for _ in range(N):
    dailyExps.append(int(stdin.readline()))

def withdrawalCount(budget):
    count = 1
    currentSum = 0
    for exp in dailyExps:
        if currentSum + exp <= budget:
            currentSum += exp
        else:
            count += 1
            currentSum = exp
    return count

def getUpperBound():
    days = N // M + 1
    current = sum(dailyExps[:days])
    for i in range(days, N):
        if dailyExps[i] > dailyExps[i - days]:
            current = current + dailyExps[i] - dailyExps[i - days]
    return current

l = max(dailyExps)
r = getUpperBound()

res = r
while l <= r:
    m = (l + r) // 2
    if withdrawalCount(m) > M:
        l = m + 1
    else:
        res = m
        r = m - 1
print(res)