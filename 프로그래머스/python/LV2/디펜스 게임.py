import heapq


def solution(n, k, enemy):
    answer = 0
    total = 0
    q = []
    for i in enemy:
        heapq.heappush(q, -i)
        total += i
        if total > n:
            if k == 0:
                break
            total += heapq.heappop(q)
            k -= 1
        answer += 1
    return answer
