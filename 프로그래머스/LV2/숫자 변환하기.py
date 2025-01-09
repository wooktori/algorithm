from collections import deque


def solution(x, y, n):
    visited = set()
    q = deque([(x, 0)])

    if x == y:
        return 0

    while q:
        present, value = q.popleft()

        for i in (present + n, present * 2, present * 3):
            if i == y:
                return value + 1
            if 1 <= i <= y and i not in visited:
                q.append((i, value + 1))
                visited.add(i)
    return -1
