from collections import deque


def bfs(j, i, land, visited, n, m):
    area = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    arr = set()
    q = deque([(j, i)])
    visited[j][i] = 1
    arr.add(i)
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                area += 1
                q.append((nx, ny))
                visited[nx][ny] = 1
                arr.add(ny)
    return [area, arr]


def solution(land):
    n = len(land)
    m = len(land[0])
    answer = [0] * m
    visited = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if not visited[j][i] and land[j][i]:
                area, arr = bfs(j, i, land, visited, n, m)
                for k in arr:
                    answer[k] += area
    return max(answer)
