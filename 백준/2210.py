import sys

input = sys.stdin.readline


def rec(x, y, ans):
    if len(ans) == 6:
        arr.append(ans)
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        else:
            rec(nx, ny, ans + board[nx][ny])


board = [list(input().split()) for _ in range(5)]
arr = []

for i in range(5):
    for j in range(5):
        rec(i, j, board[i][j])

print(len(set(arr)))
