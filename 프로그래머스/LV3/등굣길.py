def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i, j in puddles:
        dp[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or dp[i][j] == -1:
                continue
            if dp[i - 1][j] == -1:
                dp[i][j] = dp[i][j - 1]
            elif dp[i][j - 1] == -1:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]
