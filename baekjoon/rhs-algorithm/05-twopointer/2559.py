from sys import stdin

N, K = map(int, stdin.readline().split())
temps = list(map(int, stdin.readline().split()))

currentSum = sum(temps[:K])
maxSum = currentSum

for i in range(K, N):
    currentSum = currentSum + temps[i] - temps[i - K]
    maxSum = currentSum if currentSum > maxSum else maxSum

print(maxSum)
