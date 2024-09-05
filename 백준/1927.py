import sys, heapq

input = sys.stdin.readline


def sol(arr):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))


n = int(input())
arr = []
for _ in range(n):
    sol(arr)
