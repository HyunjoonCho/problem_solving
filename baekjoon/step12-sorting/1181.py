import sys 

n = int(input())

wordsList = []
for _ in range(50):
    wordsList.append([])

for _ in range(n):
    word = sys.stdin.readline()[:-1]
    if word not in wordsList[len(word) - 1]:
        wordsList[len(word) - 1].append(word)

print('\n'.join(['\n'.join(sorted(words)) for words in wordsList if words]))