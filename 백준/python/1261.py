import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]
q = []
heapq.heappush(q, (0, 0, 0))
visited[0][0] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    cost, x, y = heapq.heappop(q)
    if x == M - 1 and y == N - 1:
        print(cost)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                    heapq.heappush(q, (cost, nx, ny))
                else:
                    visited[nx][ny] = 0
                    heapq.heappush(q, (cost + 1, nx, ny))
