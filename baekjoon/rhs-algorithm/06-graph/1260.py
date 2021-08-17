import sys

rl = sys.stdin.readline

N, M, V = map(int, rl().split())
adjacencyList = [[] for _ in range(N + 1)]

for i in range(M):
    v1, v2 = map(int, rl().split())
    adjacencyList[v1].append(v2)
    adjacencyList[v2].append(v1) 
    # multiple edges may exist between two vertices

# DFS
visit = [False] * (N + 1)
def dfs(v):
    sys.stdout.write(str(v) + ' ')
    visit[v] = True
    for nextV in sorted(adjacencyList[v]):
        if not visit[nextV]:
            dfs(nextV)   
dfs(V)
sys.stdout.write('\n')

# BFS
visit = [False] * (N + 1)
queue = [V]
while queue:
    nextV = queue.pop(0)
    if not visit[nextV]:
        sys.stdout.write(str(nextV) + ' ')
        visit[nextV] = True
        queue.extend(sorted(adjacencyList[nextV]))