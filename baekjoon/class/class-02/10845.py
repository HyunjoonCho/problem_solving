from sys import stdin
rl = stdin.readline

queue = [0] * 10000
front = 0
back = 0
isEmpty = lambda x, y: 1 if x == y else 0
for _ in range(int(rl())):
    command = rl().split()
    if command[0] == 'push':
        queue[back] = command[1]
        back += 1
    elif command[0] == 'pop':
        if isEmpty(front, back):
            print(-1)
        else:
            print(queue[front])
            front += 1
    elif command[0] == 'size':
        print(back - front)
    elif command[0] == 'empty':
        print(isEmpty(front, back))
    elif command[0] == 'front':
        print(-1) if isEmpty(front, back) else print(queue[front])
    else:
        print(-1) if isEmpty(front, back) else print(queue[back - 1])