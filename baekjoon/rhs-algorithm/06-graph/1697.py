from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

queue = deque()
distList = [0] * 100001
queue.append((N))
distList[N] = 1

validate = lambda x : 0 <= x <= 100000 and not distList[x]
while queue:
    loc = queue.popleft()
    if loc == K:
        print(distList[loc] - 1)
        break
    else:
        if validate(loc - 1):
            distList[loc - 1] = distList[loc] + 1
            queue.append(loc - 1)
        if validate(loc + 1):
            distList[loc + 1] = distList[loc] + 1
            queue.append(loc + 1)
        if validate(2 * loc):
            distList[2 * loc] = distList[loc] + 1
            queue.append(2 * loc)
