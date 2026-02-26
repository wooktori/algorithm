import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
ans = [[[0, 0] for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque([(0, 0, 0)])
    ans[0][0][0] = 1

    while q:
        x, y, visited = q.popleft()

        if x == M - 1 and y == N - 1:
            return ans[y][x][visited]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if board[ny][nx] == 1 and visited == 0:
                    ans[ny][nx][1] = ans[y][x][0] + 1
                    q.append([nx, ny, 1])
                if board[ny][nx] == 0 and ans[ny][nx][visited] == 0:
                    ans[ny][nx][visited] = ans[y][x][visited] + 1
                    q.append([nx, ny, visited])
    return -1


print(bfs())
