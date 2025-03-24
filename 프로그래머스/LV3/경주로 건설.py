from collections import deque


def solution(board):
    def bfs(start):
        n = len(board)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        cost = [[int(1e9)] * n for _ in range(n)]
        cost[0][0] = 0
        q = deque([start])

        while q:
            x, y, value, direction = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:

                    if i == direction:
                        temp = value + 100
                    else:
                        temp = value + 600

                    if temp < cost[nx][ny]:
                        cost[nx][ny] = temp
                        q.append([nx, ny, temp, i])

        return cost[-1][-1]

    return min(bfs((0, 0, 0, 0)), bfs((0, 0, 0, 2)))
