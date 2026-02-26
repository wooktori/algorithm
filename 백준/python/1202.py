import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: x[0], reverse=True)
bags.sort(reverse=True)
q = []
answer = 0

while bags:
    bag = bags.pop()
    while jewels:
        weight, value = jewels.pop()
        if bag >= weight:
            heapq.heappush(q, -value)
        else:
            jewels.append([weight, value])
            break
    if q:
        answer -= heapq.heappop(q)

print(answer)
