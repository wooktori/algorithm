import sys, heapq

input = sys.stdin.readline


# def sol(arr):
#     data = list(map(int, input().split()))
#     if data[0] == 0:
#         if len(arr) == 0:
#             print(-1)
#         else:
#             maxV = max(arr)
#             print(maxV)
#             arr.remove(maxV)
#     else:
#         for i in range(1, data[0] + 1):
#             arr.append(data[i])


def sol(arr):
    data = list(map(int, input().split()))
    if data[0] == 0:
        if len(arr) == 0:
            print(-1)
        else:
            x = heapq.heappop(arr)
            print(-x)
    else:
        for i in range(1, data[0] + 1):
            heapq.heappush(arr, -data[i])


n = int(input())
arr = []
for _ in range(n):
    sol(arr)
