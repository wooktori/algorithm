from collections import deque


def div(s, e, visited, graph):
    q = deque([e])
    visited[s] = 1
    visited[e] = 1
    count = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                count += 1
    return count


def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n + 1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for s, e in wires:
        visited = [0] * (n + 1)
        temp = div(s, e, visited, graph)
        ans = abs(temp - abs(n - temp))
        answer = min(ans, answer)
    return answer
