from collections import deque


def bfs(i, n, computers, visited):
    q = deque([i])
    visited[i] = 1
    while q:
        k = q.popleft()
        for j in range(n):
            if computers[k][j] == 1 and visited[j] == 0:
                visited[j] = 1
                q.append(j)
    return 1


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    for i in range(n):
        if visited[i] == 0:
            answer += bfs(i, n, computers, visited)
    return answer
