from sys import stdin
notes = list(map(int, stdin.readline().split()))

if notes[0] == 1:
    result = 'ascending'
    for i in range(8):
        if notes[i] != (i + 1):
            result = 'mixed'
            break
elif notes[0] == 8:
    result = 'descending'
    for i in range(8):
        if notes[i] != (8 - i):
            result = 'mixed'
            break
else:
    result = 'mixed'
print(result)
