N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N - i
for i in range(K):
    result //= i + 1
print(result)