import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = list(map(int, input().split()))
items = [0]
for i in range(len(arr)):
    items.append(arr[i])


graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for i in range(N + 1):
    temp = 0
    for j in range(N + 1):
        if graph[i][j] <= M:
            temp += items[j]
    if ans < temp:
        ans = temp
print(ans)
