import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

def bfs(a,b):
    q = deque()
    q.append((a, b))
    temp = []
    temp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    temp.append((nx, ny))
    return temp

while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                team = bfs(i, j)
                if len(team) > 1:
                    flag = True
                    value = sum([board[x][y] for x, y in team]) // len(team)
                    for x, y in team:
                        board[x][y] = value
    if not flag:
        break
    ans += 1

print(ans)