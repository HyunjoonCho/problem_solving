n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

count = 0
l = 0
r = n - 1
while l < r:
    sum = nums[l] + nums[r]
    if sum == x:
        count += 1
        l += 1
        r -= 1
    elif sum < x:
        l += 1
    else:
        r -= 1

print(str(count))