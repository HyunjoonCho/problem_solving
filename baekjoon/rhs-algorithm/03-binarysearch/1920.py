N = int(input())
nums = sorted(list(map(int, input().split())))
input()
targets = list(map(int, input().split()))

def doBinarySearch(l, r, target):
    if l > r:
        return False
    else:
        m = (l + r) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            return doBinarySearch(l, m - 1, target)
        else:
            return doBinarySearch(m + 1, r, target)

def binarySearch(target):
    if doBinarySearch(0, N-1, target):
        return 1
    else:
        return 0

for target in targets:
    print(str(binarySearch(target)))