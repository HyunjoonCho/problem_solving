from sys import stdin

N = int(input())
budgets = sorted(list(map(int, stdin.readline().split())))
totalBudget = int(input())

def addBudgets(maxB):
    sum = 0
    for i in range(len(budgets)):
        if budgets[i] < maxB:
            sum += budgets[i]
        else:
            sum += (len(budgets) - i) * maxB
            break
    return sum

def search(l, r):
    if l > r:
        return r
    else:
        m = (l + r) // 2
        if addBudgets(m) == totalBudget:
            return m
        elif addBudgets(m) > totalBudget:
            return search(l, m - 1)
        else:
            return search(m + 1, r)

print(str(search(0, budgets[-1])))