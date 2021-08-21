import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
parent = [0] * (n + 1)
for _ in range(m):
    p, c = map(int, sys.stdin.readline().split())
    parent[c] = p

def parents(x):
    parents = []
    while parent[x]:
        parents.append(parent[x])
        x = parent[x]
    return parents

aParents = parents(a)
bParents = parents(b)

dist = -1
if a in bParents:
    dist = bParents.index(a) + 1
elif b in aParents:
    dist = aParents.index(b) + 1
else:
    for i in range(len(aParents)):
        for j in range(len(bParents)):
            if aParents[i] == bParents[j]:
                dist = i + j + 2
                break
        if dist != -1:
            break
print(dist)