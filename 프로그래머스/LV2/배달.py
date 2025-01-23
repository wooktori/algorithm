import heapq


def solution(N, road, K):
    answer = [1e9] * (N + 1)
    answer[1] = 0
    graph = [[] for _ in range(N + 1)]

    # (도착노드, 거리) 구조의 리스트.
    for start, end, dis in road:
        graph[start].append((end, dis))
        graph[end].append((start, dis))

    # (거리, 현재노드) 구조의 우선순위 큐.
    q = [(0, 1)]

    while q:
        distance, node = heapq.heappop(q)
        # 현재 꺼낸 거리(distance)가 이미 기록된 거리(answer[node])보다 크면 패스.
        if distance > answer[node]:
            continue

        for i in graph[node]:
            temp = distance + i[1]
            if temp < answer[i[0]]:
                answer[i[0]] = temp
                heapq.heappush(q, (temp, i[0]))

    ans = 0
    for i in range(1, len(answer)):
        if answer[i] <= K:
            ans += 1

    return ans
