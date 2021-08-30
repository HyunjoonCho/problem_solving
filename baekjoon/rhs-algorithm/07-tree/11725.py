from sys import stdin
import sys
sys.setrecursionlimit(10**5)

rl = stdin.readline

N = int(rl())
adjList = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x : int(x) - 1, rl().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [False] * N
parents = [0] * N
def dfs(v):
    for child in adjList[v]:
        if not visited[child]:
            visited[child] = True
            parents[child] = v
            dfs(child)

dfs(0)
print('\n'.join([str(x + 1) for x in parents[1:]]))