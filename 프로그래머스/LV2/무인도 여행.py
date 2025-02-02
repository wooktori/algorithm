from collections import deque


def bfs(i, j, r, c, visited, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[i][j] = 1
    q = deque([(i, j)])
    temp = int(maps[i][j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and not visited[nx][ny]
                and maps[nx][ny] != "X"
            ):
                visited[nx][ny] = 1
                q.append((nx, ny))
                temp += int(maps[nx][ny])
    return temp


def solution(maps):
    answer = []
    r = len(maps)
    c = len(maps[0])
    visited = [[0] * c for i in range(r)]

    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X" and not visited[i][j]:
                answer.append(bfs(i, j, r, c, visited, maps))

    answer.sort()

    return answer if len(answer) else [-1]
