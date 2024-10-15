import sys
from collections import deque

input = sys.stdin.readline


def left(n, m):
    if n < 0:
        return
    if board[n][2] != board[n + 1][6]:
        left(n - 1, -m)
        board[n].rotate(m)


def right(n, m):
    if n > 3:
        return
    if board[n][6] != board[n - 1][2]:
        right(n + 1, -m)
        board[n].rotate(m)


board = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    left(n - 2, -m)
    right(n, -m)
    board[n - 1].rotate(m)

ans = 0
if board[0][0] == 1:
    ans += 1
if board[1][0] == 1:
    ans += 2
if board[2][0] == 1:
    ans += 4
if board[3][0] == 1:
    ans += 8

print(ans)
