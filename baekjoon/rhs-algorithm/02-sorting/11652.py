nums = []

for i in range(int(input())):
    nums.append(int(input()))
nums.sort()

currentNum = nums[0]
currentCount = 1

maxNum = currentNum
maxCount = currentCount

for i in range(1, len(nums)):
    if nums[i] == currentNum:
        currentCount += 1
    else:
        if maxCount < currentCount:
            maxNum = currentNum
            maxCount = currentCount
        currentCount = 1
        currentNum = nums[i]

if maxCount < currentCount:
    print(currentNum)
else:
    print(maxNum)