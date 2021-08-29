from collections import deque

stack = deque()
for _ in range(int(input())):
    num = int(input())
    if not num:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))