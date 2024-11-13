import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            virus.append((board[i][j], i, j, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virus.sort()
q = deque(virus)

while q:
    value, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and not board[nx][ny]:
            q.append((value, nx, ny, time+1))
            board[nx][ny] = value

print(board[X-1][Y-1])