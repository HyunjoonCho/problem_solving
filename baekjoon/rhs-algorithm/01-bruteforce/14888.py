import sys

n = 0
nums = []
availableOps = []

def recurse(k, val):
    global min, max
    if k == n - 1:
        if val < min:
            min = val
        if val > max:
            max = val
    else:
        for i in range(4):
            if availableOps[i] > 0:
                availableOps[i] -= 1
                if i == 0:
                    recurse(k + 1, val + nums[k + 1])
                elif i == 1:
                    recurse(k + 1, val - nums[k + 1])
                elif i == 2:
                    recurse(k + 1, val * nums[k + 1])
                else:
                    if val < 0:
                        recurse(k + 1, -(-val//nums[k+1]))
                    else: 
                        recurse(k + 1, val//nums[k + 1])
                availableOps[i] += 1

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
availableOps = list(map(int, sys.stdin.readline().split()))

min = 10 ** 9 + 1
max = -(10 ** 9 + 1)

recurse(0, nums[0])

print(max)
print(min)