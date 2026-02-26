import sys

input = sys.stdin.readline


def check(board):
    count = 0
    for i in range(5):
        tempX = 0
        tempY = 0
        for j in range(5):
            if board[i][j] == 0:
                tempX += 1
            if board[j][i] == 0:
                tempY += 1
        if tempX == 5:
            count += 1
        if tempY == 5:
            count += 1

    diaX = 0
    diaY = 0
    for i in range(5):
        for j in range(5):
            if i == j and board[i][j] == 0:
                diaX += 1
            if i + j == 4 and board[i][j] == 0:
                diaY += 1
        if diaX == 5:
            count += 1
        if diaY == 5:
            count += 1

    return count


board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]


count = 0
for i in range(5):
    for j in range(5):
        x = call[i][j]
        for a in range(5):
            for b in range(5):
                if board[a][b] == x:
                    board[a][b] = 0
        count += 1

        if check(board) >= 3:
            print(count)
            sys.exit()
