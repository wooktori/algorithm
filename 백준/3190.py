import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    X, Y = map(int, input().split())
    board[X - 1][Y - 1] = 2

L = int(input())
directions = deque()
for _ in range(L):
    X, C = input().split()
    directions.append([int(X), C])

time = 0
curX, curY = 0, 0
board[curX][curY] = 1
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
point = 0
snake = deque()
snake.append((curX, curY))


def move():
    global curX, curY, point
    moveX = curX + direction[point][0]
    moveY = curY + direction[point][1]

    # 범위 초과시
    if moveX >= N or moveY >= N or moveX < 0 or moveY < 0:
        return False

    # 몸에 닿았을 시
    if board[moveX][moveY] == 1:
        return False

    snake.append((moveX, moveY))

    if board[moveX][moveY] != 2:
        X, Y = snake.popleft()
        board[X][Y] = 0

    board[moveX][moveY] = 1
    curX, curY = moveX, moveY

    return True


while True:
    time += 1

    if not move():
        break

    if directions and directions[0][0] == time:
        if directions[0][1] == "L":
            point = (point + 1) % 4
        else:
            point = (point - 1) % 4
        directions.popleft()

print(time)
