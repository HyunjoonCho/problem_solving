N = int(input())

countList = []

def count(halvedNum):
    if halvedNum < 2:
        return 1
    else:
        count = 0
        for i in range(halvedNum):
            count += countList[i] * countList[halvedNum - 1 - i]
        return count

for i in range(N // 2 + 1):
    countList.append(count(i) % 987654321)
print(countList[N // 2])