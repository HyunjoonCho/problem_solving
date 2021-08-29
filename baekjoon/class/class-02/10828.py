from sys import stdin
rl = stdin.readline

stack = [0] * 10000
top = 0
for _ in range(int(rl())):
    command = rl().split()
    if command[0] == 'push':
        stack[top] = command[1]
        top += 1
    elif command[0] == 'pop':
        if top == 0:
            print(-1)
        else:
            top -= 1
            print(stack[top])
    elif command[0] == 'size':
        print(top)
    elif command[0] == 'empty':
        print(1) if top == 0 else print(0)
    else:
        if top == 0:
            print(-1)
        else:
            print(stack[top - 1])