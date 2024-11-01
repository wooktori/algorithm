import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

maxV = max(max(graph))
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b, num, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[x][y] > num and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


for i in range(maxV):
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                temp += 1
    if temp > answer:
        answer = temp

print(answer)
