from sys import stdin

R, C = map(int, stdin.readline().split())
forestMap = []
waterLocs = []
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
currentLocs = [start]
time = 0
isReached = False
while currentLocs:
    nextWaterLocs = []
    for r, c in waterLocs:
        for dr, dc in deltas:
            nextR = r + dr
            nextC = c + dc
            if 0 <= nextR < R and 0 <= nextC < C:
                block = forestMap[nextR][nextC]
                if block == '.':
                    forestMap[nextR][nextC] = '*'
                    if (nextR, nextC) not in nextWaterLocs:
                        nextWaterLocs.append((nextR, nextC))
    
    time += 1
    nextLocs = []
    for r, c in currentLocs:
        for dr, dc in deltas:
            nextR = r + dr
            nextC = c + dc
            if (nextR, nextC) == end:
                isReached = True
                break
            if 0 <= nextR < R and 0 <= nextC < C:
                block = forestMap[nextR][nextC]
                if block == '.':
                    nextLocs.append((nextR, nextC))
        if isReached:
            break
    if isReached:
        break
    currentLocs = nextLocs
    waterLocs = nextWaterLocs

if isReached:
    print(time)
else:
    print('KAKTUS')
            
