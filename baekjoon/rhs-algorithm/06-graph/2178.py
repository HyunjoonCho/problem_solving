from sys import stdin
N, M = map(int, stdin.readline().split())

maze = []
for i in range(N):
    maze.append(list(map(int, list(stdin.readline().strip()))))

distMap = [[N * M] * M for _ in range(N)]
distMap[0][0] = 1

queue = [(0, 1, 0, 0), (1, 0, 0, 0)]
while queue:
    r, c, prevR, prevC = queue.pop(0)
    if r != -1 and r != N and c != -1 and c != M and maze[r][c]:
        if distMap[r][c] > distMap[prevR][prevC] + 1:
            distMap[r][c] = min(distMap[r][c], distMap[prevR][prevC] + 1)
            queue.append((r - 1, c, r, c))
            queue.append((r + 1, c, r, c))
            queue.append((r, c - 1, r, c))
            queue.append((r, c + 1, r, c))

print(distMap[N - 1][M - 1])        