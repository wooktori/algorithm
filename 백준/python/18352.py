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


# 11/06
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
board = [[] for _ in range(N + 1)]
dis = [1e9] * (N + 1)
dis[X] = 0

for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)

q = deque([X])
while q:
    node = q.popleft()
    for next_node in board[node]:
        if dis[next_node] == 1e9:
            dis[next_node] = dis[node] + 1
            q.append(next_node)

ans = []
for i in range(len(dis)):
    if dis[i] == K:
        ans.append(i)

if not len(ans):
    print(-1)
else:
    for i in ans:
        print(i, end=" ")
