import sys

l, c = map(int, input().split())
chars = list(sorted(list(sys.stdin.readline().split())))
vowels = ['a', 'e', 'i', 'o', 'u']

password = [0] * l
# at least 1 vowel and 2 consonants
def recurse(nextIdx, vowelCount, consonantCount):
    if vowelCount + consonantCount == l:
        if vowelCount >= 1 and consonantCount >= 2:
            print(''.join(password))
    else:
        for i in range(nextIdx, c):
            char = chars[i]
            password[vowelCount + consonantCount] = char
            if char in vowels:
                recurse(i + 1, vowelCount + 1, consonantCount)
            else:
                recurse(i + 1, vowelCount, consonantCount + 1)

recurse(0, 0, 0)