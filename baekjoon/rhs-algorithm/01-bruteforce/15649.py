import sys

n = 0
m = 0
result = []

def recurse(k):
    if k == m:
        sys.stdout.write(' '.join([str(num) for num in result]) + '\n')
    else:
        for i in [num for num in range(1, n + 1) if num not in result[:k]]:
            result[k] = i
            recurse(k + 1)

if __name__ == '__main__':
    nm = sys.stdin.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    result = [0] * m
    recurse(0)