import heapq


def solution(operations):
    answer = []
    q = []
    for i in operations:
        order, num = i.split(" ")
        num = int(num)
        if order == "I":
            heapq.heappush(q, num)
        else:
            if num == -1 and len(q):
                heapq.heappop(q)
            elif num == 1 and len(q):
                q.sort()
                q.pop()

    return [0, 0] if not len(q) else [max(q), min(q)]
