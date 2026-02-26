import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
r_graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0
            r_graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    r_graph[b][a] = 1

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            r_graph[j][i] = min(r_graph[j][i], r_graph[j][k] + r_graph[k][i])

for i in range(N + 1):
    for j in range(N + 1):
        if r_graph[i][j] != int(1e9):
            graph[i][j] = r_graph[i][j]

count = 0
for i in range(N + 1):
    temp = 0
    for j in range(N + 1):
        if graph[i][j] < int(1e9):
            temp += 1
    if temp == N:
        count += 1

print(count)
