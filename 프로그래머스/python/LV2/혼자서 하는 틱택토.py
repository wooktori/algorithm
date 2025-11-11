def bingo(board):
    now = []
    for i in range(3):
        now.append("".join(board[i]))
    for i in range(3):
        temp = ""
        for j in range(3):
            temp += board[j][i]
        now.append(temp)
    now.append(board[0][0] + board[1][1] + board[2][2])
    now.append(board[0][2] + board[1][1] + board[0][2])

    return now


def solution(board):
    oNum = 0
    xNum = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                oNum += 1
            if board[i][j] == "X":
                xNum += 1

    if not (oNum == xNum or oNum == xNum + 1):
        return 0

    state = bingo(board)
    if "OOO" in state and oNum == xNum:
        return 0
    if "XXX" in state and oNum == xNum + 1:
        return 0

    return 1
