from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    graph = defaultdict(list)

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    dis = [-1] * (n + 1)
    dis[1] = 0
    q = deque([1])

    while q:
        node = q.popleft()
        for next in graph[node]:
            if dis[next] == -1:
                dis[next] = dis[node] + 1
                q.append(next)

    return dis.count(max(dis))
