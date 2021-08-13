input()

count = {}
for s in input().split():
    if s not in count.keys():
        count[s] = 1
    else:
        count[s] += 1
input()
for s in input().split():
    if s not in count.keys():
        print('0', end=' ')
    else:
        print(count[s], end=' ')
