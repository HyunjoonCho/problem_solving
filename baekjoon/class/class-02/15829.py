from sys import stdin

L = int(stdin.readline())
r = 31
M = 1234567891

weight = []
current = 1
for _ in range(L):
    weight.append(current)
    current = current * r
    if current > M:
        current %= M

hashedVal = 0
base = ord('a') - 1

idx = 0
for c in stdin.readline().strip():
    hashedVal += (ord(c) - base) * weight[idx]
    idx += 1
print(hashedVal % M)