from sys import stdin
print(sum([x ** 2 for x in list(map(int, stdin.readline().split()))]) % 10)