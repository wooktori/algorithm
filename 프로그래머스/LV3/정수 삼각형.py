def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j + 1] = dp[i][j] + triangle[i + 1][j + 1]
            if dp[i + 1][j] == 0:
                dp[i + 1][j] = dp[i][j] + triangle[i + 1][j]
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])

    return max(dp[len(dp) - 1])
