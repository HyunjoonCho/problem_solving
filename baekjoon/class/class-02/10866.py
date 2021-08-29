from sys import stdin
rl = stdin.readline

queue = [0] * 20000
front = 10000
back = 10000
isEmpty = lambda x, y: 1 if x == y else 0
result = []
for _ in range(int(rl())):
    command = rl().split()
    if command[0] == 'push_front':
        front -=1
        queue[front] = command[1]
    elif command[0] == 'push_back':
        queue[back] = command[1]
        back += 1
    elif command[0] == 'pop_front':
        if isEmpty(front, back):
            result.append('-1')
        else:
            result.append(queue[front])
            front += 1
    elif command[0] == 'pop_back':
        if isEmpty(front, back):
            result.append('-1')
        else:
            back -= 1
            result.append(queue[back])
    elif command[0] == 'size':
        result.append(str(back - front))
    elif command[0] == 'empty':
        result.append(str(isEmpty(front, back)))
    elif command[0] == 'front':
        result.append('-1' if isEmpty(front, back) else queue[front])
    else:
        result.append('-1' if isEmpty(front, back) else queue[back - 1])
print('\n'.join(result))