import sys 

n = int(input())

userList = [[] for _ in range(200)]

for _ in range(n):
    user = sys.stdin.readline()
    userList[int(user.split()[0]) - 1].append(user)

print(''.join([''.join(users) for users in userList]))