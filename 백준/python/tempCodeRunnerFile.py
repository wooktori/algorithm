import sys
import copy

input = sys.stdin.readline


def backtrack(count):
    if count == m:
        cal()
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 3
                backtrack(count + 1)
                board[i][j] = 2


def cal():
    global answer
    copyBoard = copy.deepcopy(board)
    chicken = []
    home = []
    ans = 0

    for i in range(n):
        for j in range(n):
            if copyBoard[i][j] == 3:
                chicken.append((i, j))
            elif copyBoard[i][j] == 1:
                home.append((i, j))

    for i in home:
        distance = 1e9
        for j in chicken:
            temp = abs(i[0] - j[0]) + abs(i[1] - j[1])
            distance = min(distance, temp)
        ans += distance
    answer = min(answer, ans)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
backtrack(0)
print(answer)
