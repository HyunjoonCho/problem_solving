import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

knightC, knightR = map(lambda x : int(x) - 1, sys.stdin.readline().split())

dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

distMap = [[0] * N for _ in range(N)]
distMap[knightR][knightC] = 1
result = []

queue = deque()
queue.append((knightR, knightC))
while queue:
    r, c = queue.popleft()
    for i in range(8):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if 0 <= nextR < N and 0 <= nextC < N and not distMap[nextR][nextC]:
            distMap[nextR][nextC] = distMap[r][c] + 1
            queue.append((nextR, nextC))

for _ in range(M):
    targetC, targetR = map(lambda x : int(x) - 1, sys.stdin.readline().split())
    result.append(str(distMap[targetR][targetC] - 1))

print(' '.join(result))