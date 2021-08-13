from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

locs = list(map(int, stdin.readline().split()))

print(max([(locs[i + 1] - locs[i] + 1) // 2 for i in range(1, M - 1)] + [locs[0] - 0, N - locs[-1]]))