def solution(n):
    dp = [0, 3, 11]
    if n % 2:
        return 0
    for i in range(3, n // 2 + 1):
        dp.append((3 * dp[i - 1] + sum(dp[1 : i - 1]) * 2 + 2) % 1000000007)
    return dp[n // 2]
