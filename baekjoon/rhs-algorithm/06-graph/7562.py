from sys import stdin

T = int(stdin.readline())


for _ in range(T):
    l = int(stdin.readline())
    startR, startC = map(int, stdin.readline().split())
    endR, endC = map(int, stdin.readline().split())

    if startR == endR and startC == endC:
        print(0)
    else:
        distMap = [[-1] * l for _ in range(l)]
        queue = [(startR, startC, 0)]
        while queue:
            r, c, dist = queue.pop(0)
            if distMap[r][c] == -1:
                distMap[r][c] = dist
                if r == endR and c == endC:
                    print(dist)
                    break
                else:
                    for delR, delC in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                        if 0 <= r + delR < l and 0 <= c + delC < l:
                            queue.append((r + delR, c + delC, dist + 1))