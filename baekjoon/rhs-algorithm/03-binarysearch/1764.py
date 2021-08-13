n, m = map(int, input().split())

A = sorted([input() for _ in range(n)])
B = sorted([input() for _ in range(m)])

def binarySearch(l, r, target):
    if l > r:
        return False
    else:
        m = (l + r) // 2
        if A[m] == target:
            return True
        elif A[m] > target:
            return binarySearch(l, m - 1, target)
        else:
            return binarySearch(m + 1, r, target)

result = ''
count = 0
for b in B:
    if binarySearch(0, n - 1, b):
        count += 1
        result += '\n' + b

print(str(count) + result)
