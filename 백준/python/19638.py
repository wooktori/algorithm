import sys, heapq

input = sys.stdin.readline

n, h, t = map(int, input().split())
heights = []
ans = 0
for i in range(n):
    heapq.heappush(heights, -int(input()))

for i in range(t):
    x = -heapq.heappop(heights)
    if x < h:
        heapq.heappush(heights, -x)
        break
    elif x == 1:
        heapq.heappush(heights, -x)
    else:
        x = x // 2
        heapq.heappush(heights, -x)
        ans += 1

maxV = -heights[0]

if maxV < h:
    print("YES")
    print(ans)
else:
    print("NO")
    print(maxV)
