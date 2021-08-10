import sys

n = 0
m = 0
result = []

def recurse(k):
    if k == m:
        sys.stdout.write(' '.join([str(num) for num in result]) + '\n')
    else:
        if k == 0:
            lowerBound = 1
        else:
            lowerBound = result[k - 1] + 1

        for i in range(lowerBound, n - m + k + 2):
            result[k] = i
            recurse(k + 1)

if __name__ == '__main__':
    nm = sys.stdin.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    result = [0] * m
    recurse(0)