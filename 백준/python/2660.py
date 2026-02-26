import sys

input = sys.stdin.readline

N = int(input())
score = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            score[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    score[a][b] = 1
    score[b][a] = 1

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            score[i][j] = min(score[i][j], score[i][k] + score[k][j])


ans = []
for i in range(N + 1):
    ans.append(max(score[i][1:]))

print(min(ans), ans.count(min(ans)))
for i in range(len(ans)):
    if ans[i] == min(ans):
        print(i, end=" ")
