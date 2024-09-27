import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = True
count = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                r = nx
                c = ny
                flag = 1
                break

    if flag == 0:
        if board[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r - dx[d], c - dy[d]
