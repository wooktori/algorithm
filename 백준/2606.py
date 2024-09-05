import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
target = int(input())

graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(target):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque([x])
    count = 0
    visited[x] = 1
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                count += 1

    return count


print(bfs(1))
