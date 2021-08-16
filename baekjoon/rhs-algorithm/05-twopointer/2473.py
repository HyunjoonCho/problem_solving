from sys import stdin

N = int(stdin.readline())
feats = sorted(list(map(int, stdin.readline().split())))

totalMin = 3 * (10 ** 9)
for c in range(N - 2):
    l = c + 1
    r = N - 1
    fixedV = feats[c]
    while l < r:
        sum = feats[l] + feats[r] + fixedV
        if abs(sum) < totalMin:
            totalMin = abs(sum)
            totalTuple = (feats[l], feats[r], fixedV)
            if totalMin == 0:
                break
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1
    if totalMin == 0:
        break

print(' '.join([str(feat) for feat in sorted(totalTuple)]))
