import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]


for i in range(n):
    for j in range(5):
        for k in range(n):
            if arr[i][j] == arr[k][j]:
                check[i][k] = True

maxV = -1
ans = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if check[i][j] == True:
            temp += 1
    if temp > maxV:
        maxV = temp
        ans = i + 1

print(ans)
