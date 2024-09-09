import sys
import heapq

input = sys.stdin.readline

q = []
ans = 0
N = int(input())
for _ in range(N):
    heapq.heappush(q, int(input()))

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a + b)
    ans += a + b

print(ans)
