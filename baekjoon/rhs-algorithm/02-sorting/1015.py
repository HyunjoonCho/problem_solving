n = int(input())

A = list(map(int, input().split()))
indexedA = [(A[i], i) for i in range(n)]

indexedA.sort(key= lambda x : x[0])
P = [0] * n
for i in range(n):
    P[indexedA[i][1]] = i
print(' '.join([str(num) for num in P]))