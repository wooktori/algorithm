import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if board[nx][ny] == 1:
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[N - 1][M - 1])
