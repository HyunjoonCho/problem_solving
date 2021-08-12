import sys

n = int(input())
students = []
for _ in range(n):
    line = sys.stdin.readline().split()
    students.append([line[0]] + list(map(int, line[1:])))
students.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
print('\n'.join([student[0] for student in students]))