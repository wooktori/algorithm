import heapq


def solution(n, works):
    answer = 0
    q = []
    if n >= sum(works):
        return 0
    for work in works:
        heapq.heappush(q, -work)
    for _ in range(n):
        maxV = heapq.heappop(q)
        heapq.heappush(q, maxV + 1)

    for i in q:
        answer += i**2
    return answer
