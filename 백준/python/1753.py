import sys, heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)

graph = [[] for _ in range(V + 1)]
distance = [int(1e9)] * (V + 1)
distance[K] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, K))

while q:
    dis, node = heapq.heappop(q)
    if distance[node] < dis:
        continue
    for i in graph[node]:
        cost = dis + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for i in range(1, V + 1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
