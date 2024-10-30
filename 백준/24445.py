import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(N + 1):
    graph[i].sort(reverse=True)


def bfs(v):
    global count
    q = deque([v])
    visited[v] = count

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                count += 1
                visited[i] = count


bfs(R)

for i in range(1, N + 1):
    print(visited[i])
