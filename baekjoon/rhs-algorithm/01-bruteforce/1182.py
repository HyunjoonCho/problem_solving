from sys import stdin

n, s = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

def recurse(k, currentSum):
    global count
    if k == n:
        if currentSum == s:
            count += 1
    else:
        recurse(k + 1, currentSum)
        recurse(k + 1, currentSum + nums[k])

count = 0
recurse(0, 0)

if s == 0 or s == sum(nums):
    count -= 1

print(count)