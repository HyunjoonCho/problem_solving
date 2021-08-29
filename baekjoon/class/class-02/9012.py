from sys import stdin
from collections import deque

rl = stdin.readline
N = int(rl())

stack = deque()
for _ in range(N):
    line = rl().rstrip()
    stack.clear()
    isVPS = True
    for c in list(line):
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            isVPS = False
            break
    isVPS = not stack and isVPS
    print('YES') if isVPS else print('NO')