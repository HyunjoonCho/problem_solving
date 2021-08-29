N, K = map(int, input().split())

result =[]
table = [i + 1 for i in range(N)]

idx = 0
currentCount = N
while currentCount:
    idx = (idx + K - 1) % currentCount
    result.append(str(table.pop(idx)))
    currentCount -= 1
print('<' + ', '.join(result) + '>')