from sys import stdin
from collections import deque

rl = stdin.readline

N = int(rl())
nums = [int(rl()) - 1 for _ in range(N)]
stack = deque()

orig = 0
ops = []

for num in nums:
    if stack:
        top = stack[-1]
        if top == num:
            ops.append('-')
            stack.pop()
            continue
        elif top > num:
            ops = ['NO']
            break
    for i in range(orig, num + 1):
        stack.append(i)
        ops.append('+')
    orig = num + 1

    stack.pop()
    ops.append('-')
print('\n'.join(ops))