from sys import stdin

N = int(stdin.readline())
sentence = stdin.readline().rstrip()
sentenceLen = len(sentence)

charToIdx = lambda x : ord(x) - ord('a')
alphabetCount = lambda l : sum([1 for x in l if x != 0])

alphabets = [0] * 26

l = 0
r = 0
maxInterpretableLen = 0
while l < sentenceLen:
    c = sentence[r]
    idx = charToIdx(c)
    if not alphabets[idx]:
        if alphabetCount(alphabets) == N:
            maxInterpretableLen = max(r - l, maxInterpretableLen)
            while alphabetCount(alphabets) == N:
                alphabets[charToIdx(sentence[l])] -= 1
                l += 1
        alphabets[idx] = 1
    else:
        alphabets[idx] += 1
    r += 1
    if r == sentenceLen:
        maxInterpretableLen = max(r - l, maxInterpretableLen)
        break
print(maxInterpretableLen)