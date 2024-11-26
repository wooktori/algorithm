import sys

input = sys.stdin.readline

X = int(input())
arr = [64, 32, 16, 8, 4, 2, 1]

ans = 0
temp = 0

for i in arr:
    if temp + i <= X:
        temp += i
        ans += 1

print(ans)
