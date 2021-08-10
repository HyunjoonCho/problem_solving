from sys import stdin

input()

nums = list(map(int, stdin.readline().split()))

sortedSet = sorted(set(nums))
encoder = dict(map(lambda x : (sortedSet[x], x), range(len(sortedSet))))

print(' '.join(list(map(lambda x : str(encoder[x]), nums))))