from collections import deque


def solution(board):
    N = len(board)
    M = len(board[0])
    board = [list(i) for i in board]
    dis = [[100 for _ in range(M)] for _ in range(N)]
    startX = 0
    startY = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                startX = i
                startY = j
                dis[i][j] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(startX, startY, 0)])
    while q:
        x, y, count = q.popleft()
        if board[x][y] == "G":
            return count

        for i in range(4):
            nx = x
            ny = y
            while (
                0 <= nx + dx[i] < N
                and 0 <= ny + dy[i] < M
                and board[nx + dx[i]][ny + dy[i]] != "D"
            ):
                nx += dx[i]
                ny += dy[i]

            if dis[nx][ny] > count + 1:
                dis[nx][ny] = count + 1
                q.append((nx, ny, count + 1))
    return -1
