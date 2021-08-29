from sys import stdin
from collections import deque

rl = stdin.readline

stack = deque()
while True:
    line = rl().rstrip()
    if line == '.':
        break
    else:
        stack.clear()
        isBalanced = True
        for c in list(line):
            if c == '(' or c == '[':
                stack.append(c)
            elif c == ')' or c == ']':
                if not stack or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '['):
                    isBalanced = False
                    break
                else:
                    stack.pop()

        if isBalanced and not stack:
            print('yes')
        else:
            print('no')