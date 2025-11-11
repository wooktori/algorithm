from collections import deque


def bfs(s, e, map):
    q = deque([s])
    m = len(map)
    n = len(map[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] * n for _ in range(m)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and map[nx][ny] != "X":
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return visited[e[0]][e[1]]


def solution(maps):
    answer = 0
    maps = [list(i) for i in maps]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                mid = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)

    if bfs(start, mid, maps):
        answer += bfs(start, mid, maps)
    else:
        return -1

    if bfs(mid, end, maps):
        answer += bfs(mid, end, maps)
    else:
        return -1
    return answer


# 1. S => L 까지 가기
# 2. L => E 까지 가기
# ["SOX", "EOL"]
