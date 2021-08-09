import sys 

n = int(input())

count = [0]*8001

for _ in range(n):
    count[int(sys.stdin.readline()[:-1]) + 4000] += 1

medianCount = n//2 + 1
sum = 0
min = 8001
max = 0
maxCount = 0
isTwice = False

for i in range(8001):
    if count[i] != 0:
        sum += i * count[i]
        if i < min:
            min = i
        if i > max:
            max = i
        if maxCount == count[i] and not isTwice:
            mode = i
            isTwice = True
        if maxCount < count[i]:
            maxCount = count[i]
            mode = i
            isTwice = False
        if medianCount > 0: 
            medianCount -= count[i]
            if medianCount <= 0:
                median = i
print((sum + n//2)//n - 4000)
print(median - 4000)
print(mode - 4000)
print(max - min)