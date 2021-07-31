from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        print(f'{self._name}: {self._score}')
    def comparator(self, other):
        if self.score > other.score:
            return -1
        elif self.score < other.score:
            return 1
        else:
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            else:
                return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)