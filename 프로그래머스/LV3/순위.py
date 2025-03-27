from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)

    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    for i in range(1, n + 1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer


# 좋은 풀이
# def solution(n, results):
#     total = [["?" for i in range(n)] for j in range(n)]

#     for i in range(n):
#         total[i][i] = "SELF"

#     for result in results:
#         total[result[0] - 1][result[1] - 1] = "WIN"
#         total[result[1] - 1][result[0] - 1] = "LOSE"

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if total[i][k] == "WIN" and total[k][j] == "WIN":
#                     total[i][j] = "WIN"
#                 elif total[i][k] == "LOSE" and total[k][j] == "LOSE":
#                     total[i][j] = "LOSE"

#     answer = 0

#     for i in total:
#         if "?" not in i:
#             answer += 1

#     return answer
