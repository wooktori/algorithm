import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        dx = [1, -1, x]
        for i in range(3):
            nx = x + dx[i]
            if nx < 0 or nx > 100001:
                continue
            if 0 <= nx <= 100000 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())
dist = [0] * 100001
bfs()
