import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if arr[i][0] + i <= N:
        dp[i] = max(dp[arr[i][0] + i] + arr[i][1], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
