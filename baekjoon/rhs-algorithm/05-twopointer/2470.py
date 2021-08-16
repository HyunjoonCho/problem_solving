from sys import stdin

N = int(stdin.readline())
feats = sorted(list(map(int, stdin.readline().split())))

l = 0
r = N - 1

currentMin = 2 * (10 ** 9) + 1
while l < r:
    sum = feats[l] + feats[r]
    if not sum:
        print(feats[l], feats[r])
        break
    else:
        if abs(sum) < currentMin:
            currentMin = abs(sum)
            minPair = (feats[l], feats[r])
        if sum > 0:
            r -= 1
        else:
            l += 1

if l == r:
    print(minPair[0], minPair[1])