from sys import stdin

N = int(stdin.readline())

houseMap = []
for _ in range(N):
    houseMap.append(list(map(int, list(stdin.readline().strip()))))

visited = [[False] * N for _ in range(N)]

sizeList = []
visitQueue = []
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        else:
            # BFS?
            complexSize = 0
            visitQueue.append((i, j))
            while visitQueue:
                row, col = visitQueue.pop(0)
                if row == -1 or row == N or col == -1 or col == N:
                    continue
                if not visited[row][col]:
                    visited[row][col] = True
                    if houseMap[row][col]:
                        complexSize += 1
                        visitQueue.append((row - 1, col))
                        visitQueue.append((row + 1, col))
                        visitQueue.append((row, col - 1))
                        visitQueue.append((row, col + 1))
            if complexSize:
                sizeList.append(complexSize)
print(len(sizeList))
print('\n'.join(list(map(str, sorted(sizeList)))))