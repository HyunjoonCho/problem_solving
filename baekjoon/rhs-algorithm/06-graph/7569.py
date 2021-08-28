from sys import stdin
from collections import deque

rl = stdin.readline
C, R, H = map(int, rl().split())

tomatoBoxes = []
unripeCount = 0
ripeOnes = deque()
for h in range(H):
    box = []
    for r in range(R):
        row = list(map(int, rl().split()))
        box.append(row)
        for c in range(C):
            if row[c] == 0:
                unripeCount += 1
            elif row[c] == 1:
                ripeOnes.append((h, r, c))
    tomatoBoxes.append(box)

visited = [[[False] * C for _ in range(R)] for _ in range(H)]

dh = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1] 
days = 0
while unripeCount and ripeOnes:
    currentLen = len(ripeOnes)
    for _ in range(currentLen):
        h, r, c = ripeOnes.popleft()
        visited[h][r][c] = True
        for i in range(6):
            nextH = h + dh[i]
            nextR = r + dr[i]
            nextC = c + dc[i]
            if (0 <= nextH < H and 0 <= nextR < R and 0 <= nextC < C 
                and not visited[nextH][nextR][nextC] and not tomatoBoxes[nextH][nextR][nextC]):
                    unripeCount -= 1
                    if not unripeCount:
                        break
                    tomatoBoxes[nextH][nextR][nextC] = 1
                    ripeOnes.append((nextH, nextR, nextC))
        if not unripeCount:
            break
    days += 1

if not unripeCount:
    print(days)
else:
    print(-1)