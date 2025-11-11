from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0] * len(words)
    q = deque()
    q.append([begin, 0])

    while q:
        now, count = q.popleft()

        if target == now:
            return count

        for i in range(len(words)):
            level = 0
            for j in range(len(now)):
                if words[i][j] != now[j]:
                    level += 1

            if level == 1 and visited[i] == 0:
                q.append([words[i], count + 1])
                visited[i] = 1

    return 0
