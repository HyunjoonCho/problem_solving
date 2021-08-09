import math

def factorize(n):
    upperBound = int(math.sqrt(n))

    factor = 2
    while factor <= upperBound and n != 1:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 1
    if n != 1:
        print(n)    

if __name__ == '__main__':    
    factorize(int(input()))