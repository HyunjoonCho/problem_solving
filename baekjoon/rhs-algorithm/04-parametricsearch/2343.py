from sys import stdin

N, M = map(int, stdin.readline().split())
lectures = list(map(int, stdin.readline().split()))

def diskCount(length):
    count = 1
    currentSum = 0
    for lecture in lectures:
        if currentSum + lecture > length:
            count += 1
            currentSum = lecture
        else:
            currentSum += lecture
    return count

l = max(lectures)
r = sum(lectures)

res = r
while l <= r:
    m = (l + r) // 2
    if diskCount(m) > M:
        l = m + 1
    else:
        res = m
        r = m - 1
print(res)