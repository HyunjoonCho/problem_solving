from sys import stdin

N, M = map(int, stdin.readline().split())
n = list(map(int, stdin.readline().split()))
m = list(map(int, stdin.readline().split()))

idxN = 0
idxM = 0
merged = []
while idxN < N or idxM < M:
    if idxN == N:
        merged += m[idxM:]
        break
    elif idxM == M:
        merged += n[idxN:]
        break
    else:
        if n[idxN] <= m[idxM]:
            merged.append(n[idxN])
            idxN += 1
        else:
            merged.append(m[idxM])
            idxM += 1

print(' '.join([str(num) for num in merged]))