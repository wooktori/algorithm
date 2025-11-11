from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    answer = []
    cost = [int(1e9)] * (n + 1)
    q = deque([destination])
    dic = defaultdict(list)

    for a, b in roads:
        dic[a].append(b)
        dic[b].append(a)

    cost[destination] = 0

    while q:
        node = q.popleft()
        for i in dic[node]:
            if cost[i] > cost[node] + 1:
                cost[i] = cost[node] + 1
                q.append(i)

    for i in sources:
        if cost[i] == int(1e9):
            answer.append(-1)
        else:
            answer.append(cost[i])
    return answer
