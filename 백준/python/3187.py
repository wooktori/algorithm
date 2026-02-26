import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
wolf = 0
sheep = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == "v":
            wolf += 1
        elif board[i][j] == "k":
            sheep += 1
