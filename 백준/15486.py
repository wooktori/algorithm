import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + arr[i - 1][0] <= N + 1:
        dp[i + arr[i - 1][0] - 1] = max(
            dp[i - 1] + arr[i - 1][1], dp[i + arr[i - 1][0]]
        )

print(dp[-1])
