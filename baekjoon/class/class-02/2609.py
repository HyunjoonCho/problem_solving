a, b = map(int, input().split())

p, q = (a, b) if a > b else (b, a)
while q:
    p, q = q, p % q
print(p, a * b // p, sep='\n')