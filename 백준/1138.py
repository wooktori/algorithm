import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if arr[i] == count and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            count += 1

for i in ans:
    print(i, end=" ")
