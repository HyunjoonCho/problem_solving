n, m = map(int, input().split())
nums = list(sorted(list(map(int, input().split()))))
isUsed = [False] * n

seq = [0] * m
results = []

def recurse(k):
    if k == m:
        seqStr = ' '.join([str(num) for num in seq])
        if seqStr not in results:
            results.append(seqStr)
    else:
        for i in range(n):
            if not isUsed[i]:
                isUsed[i] = True
                seq[k] = nums[i]
                recurse(k + 1)
                isUsed[i] = False

recurse(0)
for seq in results:
    print(seq)