import sys 

n = int(input())

count = [0]*10001

for _ in range(n):
    count[int(sys.stdin.readline()[:-1])] += 1

for i in range(10001):
    for _ in range(count[i]):
        sys.stdout.write(str(i) + '\n')