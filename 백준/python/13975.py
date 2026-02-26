import sys, heapq

input = sys.stdin.readline


def sol():
    k = int(input())
    data = list(map(int, input().split()))
    heapq.heapify(data)
    count = 0

    while len(data) > 1:
        x = heapq.heappop(data)
        y = heapq.heappop(data)
        count += x + y
        heapq.heappush(data, x + y)
    print(count)


t = int(input())
for _ in range(t):
    sol()
