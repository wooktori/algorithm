import sys

input = sys.stdin.readline


def chicken_len(house_x, house_y, chicken_x, chicken_y):
    return abs(house_x - chicken_x) + abs(house_y - chicken_y)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append((i, j))
        if board[i][j] == 2:
            chickens.append((i, j))
