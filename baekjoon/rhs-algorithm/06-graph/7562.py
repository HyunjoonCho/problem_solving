from sys import stdin
from collections import deque

T = int(stdin.readline())
deltas = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

for _ in range(T):
    l = int(stdin.readline())
    startR, startC = map(int, stdin.readline().split())
    endR, endC = map(int, stdin.readline().split())

    distMap = [[0] * l for _ in range(l)]
    queue = deque()
    queue.append((startR, startC))
    distMap[startR][startC] = 1
    while queue:
        r, c = queue.popleft()
        if r == endR and c == endC:
            print(distMap[r][c] - 1)
            break
        else:
            for delR, delC in deltas:
                nextR = r + delR
                nextC = c + delC
                if 0 <= nextR < l and 0 <= nextC < l and not distMap[nextR][nextC]:
                    distMap[nextR][nextC] = distMap[r][c] + 1
                    queue.append((nextR, nextC))