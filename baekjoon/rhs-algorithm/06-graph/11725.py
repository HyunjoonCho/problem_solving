import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
adjList = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

parent = [0] * (N + 1)

def dfs(v):
    for nextV in adjList[v]:
        if nextV == parent[v]:
            continue
        parent[nextV] = v
        dfs(nextV)

dfs(1)
print('\n'.join(map(str, parent[2:])))