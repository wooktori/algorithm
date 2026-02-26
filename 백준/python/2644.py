import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
board = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = -1

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)


def dfs(node, num):
    global ans
    visited[node] = True

    if node == b:
        ans = num

    for i in board[node]:
        if not visited[i]:
            dfs(i, num + 1)


dfs(a, 0)
print(ans)
