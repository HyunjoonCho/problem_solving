n = int(input())

words = set()
for i in range(n):
    words.add(input())
words = list(words)
words.sort(key= lambda x : (len(x), x))
print('\n'.join(words))
# previous solution in ../step-by-step/stp12-sorting 