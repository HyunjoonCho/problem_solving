from sys import stdin

N, M = map(int, stdin.readline().split())

adjacencyList = [[] for _ in range(N + 1)] # vertex ranges from 1 to N, NOT 0
for _ in range(M):
    v1, v2 = map(int, stdin.readline().split())
    adjacencyList[v1].append(v2)
    adjacencyList[v2].append(v1)

def dfs(v):
    if not visited[v]:
        visited[v] = True
        for nextV in adjacencyList[v]:
            dfs(nextV)

connectedComponentsCount = 0
visited = [False for _ in range(N + 1)]
for v in range(1, N + 1):
    if not visited[v]:
        connectedComponentsCount += 1
        dfs(v) # BFS timed-out! Why? What if most vertices are connected..

print(connectedComponentsCount)
# May use Tree to make it faster