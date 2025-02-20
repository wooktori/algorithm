from collections import deque


def solution(players, m, k):
    answer = 0
    q = deque()
    for i in range(24):
        if len(q) == k:
            q.popleft()
        server = players[i] // m
        using_server = sum(q)
        add_server = server - using_server
        if add_server > 0:
            q.append(add_server)
            answer += add_server
        else:
            q.append(0)
    return answer
