from sys import stdin

V = int(stdin.readline())

adjMtrx = []
for _ in range(V):
    adjMtrx.append(list(map(int, stdin.readline().split())))

def dfs(v, visited):
    if not visited[v]:
        visited[v] = 1
        for nextV in [x for x in range(V) if adjMtrx[v][x]]:
            visited = dfs(nextV, visited)   
    return visited

for i in range(V):
    visited = [0] * V
    for nextV in [x for x in range(V) if adjMtrx[i][x]]:
        visited = dfs(nextV, visited)
    print(' '.join(list(map(str, visited))))