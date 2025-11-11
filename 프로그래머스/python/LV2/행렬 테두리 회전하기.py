def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for i in queries:
        minV = 10000
        x1, y1, x2, y2 = i
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        t1 = board[x1][y2]
        t2 = board[x2][y2]
        t3 = board[x2][y1]
        t4 = board[x1][y1]
        minV = min(minV, t1, t2, t3, t4)
        for i in range(y2, y1, -1):
            board[x1][i] = board[x1][i - 1]
            minV = min(minV, board[x1][i])
        for i in range(x2, x1, -1):
            board[i][y2] = board[i - 1][y2]
            minV = min(minV, board[i][y2])
        for i in range(y1, y2):
            board[x2][i] = board[x2][i + 1]
            minV = min(minV, board[x2][i])
        for i in range(x1, x2):
            board[i][y1] = board[i + 1][y1]
            minV = min(minV, board[i][y1])
        board[x1 + 1][y2] = t1
        board[x2][y2 - 1] = t2
        board[x2 - 1][y1] = t3
        board[x1][y1 + 1] = t4
        answer.append(minV)
    return answer
