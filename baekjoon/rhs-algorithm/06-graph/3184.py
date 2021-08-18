from sys import stdin

R, C = map(int, stdin.readline().split())
farmMap = list(map(list, stdin.read(R * (C + 1)).split()))

visited = [[False] * C for _ in range(R)]
totalSheepCount = 0
totalWolfCount = 0
for i in range(R):
    for j in range(C):
        queue = [(i, j)]
        sheepCount = 0
        wolfCount = 0
        while queue:
            r, c = queue.pop(0)
            if r != -1 and r != R and c != -1 and c != C and not visited[r][c]:
                visited[r][c] = True
                if farmMap[r][c] == '#':
                    continue
                elif farmMap[r][c] == 'o':
                    sheepCount += 1
                elif farmMap[r][c] == 'v':
                    wolfCount += 1
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
        if sheepCount > wolfCount:
            totalSheepCount += sheepCount
        else:
            totalWolfCount += wolfCount
print(totalSheepCount, totalWolfCount)