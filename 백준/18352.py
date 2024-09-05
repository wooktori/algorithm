import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
dict = {}

# 딕셔너리 value => 배열로 초기화
for i in range(n + 1):
    dict[i] = []

# 딕셔너리에 연결된 도시 추가
for _ in range(m):
    a, b = map(int, input().split())
    dict[a].append(b)

distance = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

q = deque([x])
visited[x] = 1

while q:
    city = q.popleft()
    for i in dict[city]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            distance[i] = distance[city] + 1

ans = 0
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        ans += 1
if ans == 0:
    print(-1)
