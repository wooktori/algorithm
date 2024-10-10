import sys

input = sys.stdin.readline


# 백트래킹
def backtrack(count, start):
    # 치킨집이 m개가 되면 거리 계산
    if count == m:
        cal()
        return

    # 선택된 치킨집 이후의 치킨집들만 탐색
    for i in range(start, len(chicken)):
        if not visited[i]:
            visited[i] = True
            backtrack(count + 1, i + 1)
            visited[i] = False


# 집과 치킨집의 거리 계산 로직
def cal():
    global answer
    ans = 0

    for i in home:
        distance = 1e9
        for j in range(len(chicken)):
            if visited[j]:
                temp = abs(i[0] - chicken[j][0]) + abs(i[1] - chicken[j][1])
                distance = min(distance, temp)
        ans += distance
    answer = min(answer, ans)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
chicken = []
home = []
visited = [False] * 13

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))
        elif board[i][j] == 1:
            home.append((i, j))

backtrack(0, 0)
print(answer)
