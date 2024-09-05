import sys
from collections import deque

input = sys.stdin.readline


def sol():
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    board = [[0] * l for _ in range(l)]
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    def bfs():
        q = deque()
        q.append((x1, y1))

        while q:
            x, y = q.popleft()
            if x == x2 and y == y2:
                return board[x][y]
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1

    print(bfs())


t = int(input())

for _ in range(t):
    sol()
