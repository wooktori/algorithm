import sys

sys.setrecursionlimit(10**6)
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
    graph[i].sort()


def dfs(v):
    global count
    visited[v] = count

    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(i)


dfs(R)

for i in range(1, N + 1):
    print(visited[i])
