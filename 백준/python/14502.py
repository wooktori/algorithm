import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0


def bfs():
    global ans

    q = deque()
    copyBoard = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if copyBoard[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and copyBoard[nx][ny] == 0:
                copyBoard[nx][ny] = 2
                q.append((nx, ny))

    temp = 0

    for i in range(N):
        for j in range(M):
            if copyBoard[i][j] == 0:
                temp += 1

    ans = max(ans, temp)


def wall(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count + 1)
                board[i][j] = 0


wall(0)
print(ans)
