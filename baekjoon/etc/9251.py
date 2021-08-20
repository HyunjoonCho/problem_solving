import sys

A = ' ' + sys.stdin.readline().strip()
B = ' ' + sys.stdin.readline().strip()

a = len(A)
b = len(B)

table = [[0] * a for _ in range(b)]

for i in range(1, b):
    for j in range(1, a):
        if A[j] == B[i]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])
print(table[b - 1][a - 1])