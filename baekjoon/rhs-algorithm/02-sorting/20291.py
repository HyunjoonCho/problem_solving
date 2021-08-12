n = int(input())

exts = []
for i in range(n):
    fileName = input()
    exts.append(fileName.split('.')[1])
exts.sort()

currentExt = exts[0]
count = 1
for i in range(1, n):
    if currentExt == exts[i]:
        count += 1
    else:
        print(currentExt, count)
        currentExt = exts[i]
        count = 1
print(currentExt, count)