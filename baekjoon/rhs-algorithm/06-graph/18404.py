import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

knightC, knightR = map(int, sys.stdin.readline().split())

dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

distMap = [[0] * (N + 1) for _ in range(N + 1)]
distMap[knightR][knightC] = 1
queue = deque()
for _ in range(M):
    targetC, targetR = map(int, sys.stdin.readline().split())

    if distMap[targetR][targetC]:
        sys.stdout.write(str(distMap[targetR][targetC] - 1))
    else:
        queue.append((knightR, knightC))
        while queue:
            r, c = queue.popleft()
            if r == targetR and c == targetC:
                sys.stdout.write(str(distMap[r][c] - 1))
                break
            else:
                for i in range(8):
                    nextR = r + dr[i]
                    nextC = c + dc[i]
                    if 1 <= nextR <= N and 1 <= nextC <= N:
                        if not distMap[nextR][nextC]:
                            distMap[nextR][nextC] = distMap[r][c] + 1
                        queue.append((nextR, nextC))
        queue.clear()
    sys.stdout.write(' ')