from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())
forestMap = []
waterLocs = deque()
for i in range(R):
    forestMap.append(list(stdin.readline().strip()))
    for j in range(C):
        if forestMap[i][j] == '*':
            waterLocs.append((i, j))
        elif forestMap[i][j] == 'S':
            start = (i, j)
            forestMap[i][j] = '.'
        elif forestMap[i][j] == 'D':
            end = (i, j)
            forestMap[i][j] = 'X'

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

currentLocs = deque()
currentLocs.append(start)
time = 0
isReached = False
visited = [[False] * C for _ in range(R)]
visited[start[0]][start[1]] = True
while currentLocs:
    waterLen = len(waterLocs)
    for _ in range(waterLen):
        r, c = waterLocs.popleft()
        for dr, dc in deltas:
            nextR = r + dr
            nextC = c + dc
            if 0 <= nextR < R and 0 <= nextC < C:
                block = forestMap[nextR][nextC]
                if block == '.':
                    forestMap[nextR][nextC] = '*'
                    waterLocs.append((nextR, nextC))
    
    time += 1
    locsLen = len(currentLocs)
    for _ in range(locsLen):
        r, c = currentLocs.popleft()
        for dr, dc in deltas:
            nextR = r + dr
            nextC = c + dc
            if (nextR, nextC) == end:
                isReached = True
                break
            if 0 <= nextR < R and 0 <= nextC < C and not visited[nextR][nextC]:
                visited[nextR][nextC] = True
                block = forestMap[nextR][nextC]
                if block == '.':
                    currentLocs.append((nextR, nextC))
        if isReached:
            break
    if isReached:
        break

if isReached:
    print(time)
else:
    print('KAKTUS')