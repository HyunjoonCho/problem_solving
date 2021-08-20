from sys import stdin
from copy import deepcopy

N, M = map(int, stdin.readline().split())

originalMap = []
for _ in range(N):
    originalMap.append(list(map(int, stdin.readline().split())))

vacancies = []
viruses = []
for i in range(N):
    for j in range(M):
        if originalMap[i][j] == 0:
            vacancies.append((i, j))
        elif originalMap[i][j] == 2:
            viruses.append((i, j))

def spread(newMap):
    visited = [[False] * M for _ in range(N)]
    queue = list(viruses)
    while queue:
        nextR, nextC = queue.pop(0)
        if nextR != -1 and nextR != N and nextC != -1 and nextC != M and not visited[nextR][nextC]:
            visited[nextR][nextC] = True
            if newMap[nextR][nextC] != 1:
                newMap[nextR][nextC] = 2
                queue.append((nextR - 1, nextC))
                queue.append((nextR + 1, nextC))
                queue.append((nextR, nextC - 1))
                queue.append((nextR, nextC + 1))
    return newMap

vacCount = len(vacancies)
maxSafetyZone = 0
for i in range(vacCount):
    firstR, firstC = vacancies[i]
    originalMap[firstR][firstC] = 1
    for j in range(i + 1, vacCount):
        secondR, secondC = vacancies[j]
        originalMap[secondR][secondC] = 1
        for k in range(j + 1, vacCount):
            thirdR, thirdC = vacancies[k]
            originalMap[thirdR][thirdC] = 1
            newMap = spread(deepcopy(originalMap))
            safetyZone = sum([row.count(0) for row in newMap])
            maxSafetyZone = max(maxSafetyZone, safetyZone)
            originalMap[thirdR][thirdC] = 0
        originalMap[secondR][secondC] = 0
    originalMap[firstR][firstC] = 0
print(maxSafetyZone)