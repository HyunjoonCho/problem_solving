import sys

A, B, C = map(int, sys.stdin.readline().split())

visited = []

def pour(x, y, ySize):
    if x <= ySize - y:
        return 0, x + y
    else:
        return x - (ySize - y), ySize

def dfs(state):
    if state not in visited:
        a, b, c = state
        visited.append(state)
        newA, newB = pour(a, b, B)
        dfs((newA, newB, c))
        newA, newC = pour(a, c, C)
        dfs((newA, b, newC))
        newB, newA = pour(b, a, A)
        dfs((newA, newB, c))
        newB, newC = pour(b, c, C)
        dfs((a, newB, newC))
        newC, newA = pour(c, a, A)
        dfs((newA, b, newC))
        newC, newB = pour(c, b, B)
        dfs((a, newB, newC))

dfs((0, 0, C))
print(' '.join(list(map(str, sorted(set([x[2] for x in visited if x[0] == 0]))))))