from collections import deque
N = int(input())

nums = deque([i for i in range(N)])
while len(nums) != 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums.popleft() + 1)