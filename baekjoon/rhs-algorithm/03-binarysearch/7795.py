T = int(input())

def countPairs(A, B):
    count = 0

    idx = 0
    bLen = len(B)
    for a in A:
        while idx != bLen and B[idx] < a:
            idx += 1
        count += idx
    return count

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    print(str(countPairs(A, B)))

# Expected Sol) sort M then do binary search for a in A