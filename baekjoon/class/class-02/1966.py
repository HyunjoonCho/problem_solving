from sys import stdin
from collections import deque

rl = stdin.readline
T = int(rl())

for _ in range(T):
    N, target = map(int, rl().split())
    priorities = list(map(int, rl().split()))

    priorityCount = [0] * 10
    queue = deque()
    idx = 0
    for p in priorities:
        priorityCount[p] += 1
        queue.append((p, idx))
        idx += 1

    def maxPriority():
        idx = 9
        for count in reversed(priorityCount):
            if count:
                return idx
            else:
                idx -= 1

    printCount = 0
    while True:
        maxP = maxPriority()
        priority, idx = queue.popleft()
        if priority == maxP:
            printCount += 1
            priorityCount[priority] -= 1
            if idx == target:
                print(printCount)
                break
        else:
            queue.append((priority, idx))