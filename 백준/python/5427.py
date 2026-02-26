# import sys
# from collections import deque

# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]


# def bfs():
#     while q:
#         x, y = q.popleft()
#         if visited[x][y] != "FIRE":
#             flag = visited[x][y]
#         else:
#             flag = "FIRE"

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < h and 0 <= ny < w:
#                 if building[nx][ny] == "." and visited[nx][ny] == 0:
#                     if flag == "FIRE":
#                         visited[nx][ny] = "FIRE"
#                     else:
#                         visited[nx][ny] = flag + 1
#                     q.append((nx, ny))
#             else:
#                 if flag != "FIRE":
#                     return flag

#     return "IMPOSSIBLE"


# t = int(input())
# for _ in range(t):
#     w, h = map(int, input().split())
#     building = [list(input().rstrip()) for _ in range(h)]
#     visited = [[False] * w for _ in range(h)]
#     q = deque()

#     for i in range(h):
#         for j in range(w):
#             if building[i][j] == "@":
#                 mq.append((i, j, t))
#                 visited[i][j] = True
#             elif building[i][j] == "*":
#                 fq.append((i, j, t))

from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == "." and visited[nx][ny] == 0:
                    if flag == "FIRE":
                        visited[nx][ny] = "FIRE"
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag

    return "IMPOSSIBLE"


for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    q = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == "@":
                start = (i, j)
                board[i][j] = "."
                visited[i][j] = 1
            elif board[i][j] == "*":
                visited[i][j] = "FIRE"
                q.append((i, j))

    q.append(start)
    print(bfs())
