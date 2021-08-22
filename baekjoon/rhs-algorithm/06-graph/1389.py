from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
adjList = [[] for _ in range(N)]

for _ in range(M):
    usr1, usr2 = map(lambda x : int(x) - 1, stdin.readline().split())
    if usr2 not in adjList[usr1]:
        adjList[usr1].append(usr2)
        adjList[usr2].append(usr1)

distMap = [[N] * N for _ in range (N)]
queue = deque()
for usr in range(N):
    queue.append(usr)
    distMap[usr][usr] = 0
    while queue:
        currUsr = queue.popleft()
        dist = distMap[usr][currUsr] + 1
        for friend in adjList[currUsr]:
            if distMap[usr][friend] > dist:
                distMap[usr][friend] = dist
                distMap[friend][usr] = dist
                queue.append(friend)

currUsr = 0
minDist = 10000

for i in range(N):
    sumDist = sum(distMap[i])
    if sumDist < minDist:
        currUsr = i
        minDist = sumDist
print(currUsr + 1)