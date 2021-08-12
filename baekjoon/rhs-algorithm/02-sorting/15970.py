import sys

N = int(input())

coloredPts = {}
for _ in range(N):
    pt = sys.stdin.readline().split()
    if pt[1] in coloredPts.keys():
        coloredPts[pt[1]].append(int(pt[0]))
    else:
        coloredPts[pt[1]] = [int(pt[0])]

sum = 0
for key in coloredPts.keys():
    pts = coloredPts[key]
    pts.sort()
    sum += pts[1] - pts[0]
    for i in range(1, len(pts) - 1):
        sum += min(pts[i] - pts[i - 1], pts[i + 1] - pts[i])
    sum += pts[-1] - pts[-2]

print(sum)