from sys import stdin

N = int(stdin.readline())
E = int(stdin.readline())

adjMtrx = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    v1, v2 = map(int, stdin.readline().split())
    adjMtrx[v1][v2] = 1
    adjMtrx[v2][v1] = 1

visited = [0] * (N + 1)

def dfs(v):
    if not visited[v]:
        visited[v] = 1
        for nextV in [x for x in range(1, N + 1) if adjMtrx[v][x]]:
            dfs(nextV)

dfs(1)
print(sum([1 for i in range(2, N + 1) if visited[i]]))