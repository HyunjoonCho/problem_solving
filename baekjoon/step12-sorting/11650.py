import sys 

n = int(input())

coords = []
for _ in range(n):
    coord = list(map(int, sys.stdin.readline().split()))
    coords.append((coord[0] + 100000) * 200000 + coord[1] + 100000)

for coord in sorted(coords):
    sys.stdout.write(str(coord // 200000 - 100000) + ' ' + str(coord % 200000 - 100000) + '\n')