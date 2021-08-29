from sys import stdin
rl = stdin.readline

R, C, B = map(int, rl().split())
heightMap = []
for _ in range(R):
    heightMap.append(list(map(int, rl().split())))

minH = min([min(row) for row in heightMap])
maxH = max([max(row) for row in heightMap])

minTimeCount = 500 * 500 * 2 * 128
minTimeHeight = 0
for H in range(minH, maxH + 1):
    timeCount = 0
    currentBlock = B
    for row in heightMap:
        for h in row:
            if h > H:
                timeCount += 2 * (h - H)
                currentBlock += h - H
            
    for row in heightMap:
        for h in row:
            if h < H:
                if currentBlock >= H - h:
                    timeCount += H - h
                    currentBlock -= H - h
                else: 
                    timeCount = 500 * 500 * 2 * 128
                    break
    if minTimeCount >= timeCount:
        minTimeCount = timeCount
        minTimeHeight = H

print(minTimeCount, minTimeHeight)