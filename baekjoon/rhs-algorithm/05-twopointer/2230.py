from sys import stdin 

N, M = map(int, stdin.readline().split())

nums = []
for _ in range(N):
    nums.append(int(stdin.readline()))
nums.sort()

l = 0
r = 0
minGeqM = 2 * (10 ** 9) + 1

while r < N - 1:
    r += 1
    diff = nums[r] - nums[l]
    if diff >= M:
        while l < r:
            diff = nums[r] - nums[l]
            if diff >= M:
                minGeqM = min(diff, minGeqM) 
            else:
                break
            l += 1

print(minGeqM)       
