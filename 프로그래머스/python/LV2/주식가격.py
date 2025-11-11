from collections import deque


def solution(prices):
    result = []
    queue = deque(prices)

    while queue:
        time = 0
        price = queue.popleft()

        for q in queue:
            time += 1
            if price > q:
                break
        result.append(time)

    return result
