import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and board[x][y] == board[nx][ny]
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append((nx, ny))


N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans = 0
ans2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == "G":
            board[i][j] = "R"

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans2 += 1

print(ans, ans2)
