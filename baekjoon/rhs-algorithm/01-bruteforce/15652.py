import sys

n = 0
m = 0
result = []

def recurse(k):
    if k == m:
        sys.stdout.write(' '.join([str(num) for num in result]) + '\n')
    else:
        if k == 0:
            for i in range(1, n + 1):
                result[0] = i
                recurse(1)
        else :
            for i in range(result[k - 1], n + 1):
                result[k] = i
                recurse(k + 1)

if __name__ == '__main__':
    nm = sys.stdin.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    result = [0] * m
    recurse(0)