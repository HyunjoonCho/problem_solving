from sys import stdin 

T = int(stdin.readline())

def countClusters(cabbageMap, M, N):
    visited = [[False] * N for _ in range(M)]
    queue = []
    clusterCount = 0
    for i in range(M):
        for j in range(N):
            queue.append((i, j))
            isNewCluster = False
            while queue:
                x, y = queue.pop(0)
                if x == -1 or x == M or y == -1 or y == N or visited[x][y]:
                    continue
                visited[x][y] = True
                if cabbageMap[x][y]:
                    isNewCluster = True
                    queue.append((x - 1, y))
                    queue.append((x + 1, y))
                    queue.append((x, y - 1))
                    queue.append((x, y + 1))
            if isNewCluster:
                clusterCount += 1
    return clusterCount

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    cabbageMap = [[False] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        cabbageMap[x][y] = True
    print(countClusters(cabbageMap, M, N))
    