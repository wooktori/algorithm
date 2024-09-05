# import sys

# input = sys.stdin.readline

# N, M, B = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# time = int(1e9)
# index = 0

# for x in range(257):
#     ans = 0
#     inven = B
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] > x:
#                 ans += 2 * (arr[i][j] - x)
#                 inven += arr[i][j] - x
#             else:
#                 ans += x - arr[i][j]
#                 inven -= x - arr[i][j]

#     if inven >= 0 and time >= ans:
#         time = ans
#         index = x

# print(time, index)

import sys

N, M, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = int(1e9)
index = 0

for x in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(N):
        for j in range(M):

            if arr[i][j] > x:
                exceed_block += arr[i][j] - x
            else:
                lack_block += x - arr[i][j]

    if exceed_block + B >= lack_block:
        if (exceed_block * 2) + lack_block <= answer:
            answer = (exceed_block * 2) + lack_block
            index = x


print(answer, index)
