from sys import stdin

K, N = map(int, stdin.readline().split())

lans = []
for _ in range(K):
    lans.append(int(stdin.readline()))

def countLans(llen):
    return sum([l//llen for l in lans])

l = 0
r = sum(lans)//K

while l <= r:
    m = (l + r) // 2
    if m == 0:
        l = r = 1
    elif countLans(m) < N:
        r = m - 1
    else:
        l = m + 1

print(str(r))