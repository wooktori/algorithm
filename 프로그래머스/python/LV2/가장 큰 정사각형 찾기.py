def solution(board):
    answer = 0
    r = len(board) + 1
    c = len(board[0]) + 1

    dp = [[0] * c for _ in range(r)]

    for i in range(1, r):
        for j in range(1, c):
            if board[i - 1][j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            answer = max(answer, dp[i][j])

    return answer**2
