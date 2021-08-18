from sys import stdin

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break

    seaMap = []
    for i in range(h):
        seaMap.append(list(map(int, stdin.readline().split())))
    visited = [[False] * w for _ in range(h)]

    islandCount = 0
    for j in range(h):
        for i in range(w):
            isIsland = False
            queue = [(j, i)]
            while queue:
                y, x = queue.pop(0)
                if y != -1 and y != h and x != -1 and x != w and not visited[y][x]:
                    visited[y][x] = True
                    if seaMap[y][x]:
                        isIsland = True
                        queue.append((y - 1, x - 1))
                        queue.append((y - 1, x))
                        queue.append((y - 1, x + 1))
                        queue.append((y, x + 1))
                        queue.append((y + 1, x + 1))
                        queue.append((y + 1, x))
                        queue.append((y + 1, x - 1))
                        queue.append((y, x - 1))
            if isIsland:
                islandCount += 1
    print(islandCount)
