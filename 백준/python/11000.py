import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

ans = [arr[0][1]]
for i in range(1, N):
    if ans[0] <= arr[i][0]:
        heapq.heappop(ans)
    heapq.heappush(ans, arr[i][1])

print(len(ans))
