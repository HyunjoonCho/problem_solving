n = int(input())

def checkCoords(bound):
    for i in range(bound):
        if abs(coords[i] - coords[bound]) == bound - i:
                return False
    return True

def recurse(k):
    global count, coords
    if k == n:
        count += 1
    else:
        for i in range(n):
            if i not in coords:
                coords[k] = i
                if checkCoords(k):
                    recurse(k + 1)
                coords[k] = -1
        
coords = [-1] * n
count = 0
recurse(0)
print(count)