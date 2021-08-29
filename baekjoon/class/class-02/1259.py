from sys import stdin
rl = stdin.readline

while True:
    num = rl().strip()
    if num == '0':
        break
    numLen = len(num)
    result = 'yes'
    for i in range(numLen//2):
        if num[i] != num[numLen - 1 - i]:
            result = 'no'
            break
    print(result)