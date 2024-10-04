import sys

input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))
dict = {}
answer = ""
# 등장 순서
count = 1

for i in arr:
    if i in dict:
        dict[i][0] += 1
    else:
        dict[i] = [1, count]
        count += 1


sortedArr = sorted(dict.items(), key=lambda x: [-x[1][0], x[1][1]])

for key, value in sortedArr:
    answer += (str(key) + " ") * value[0]

print(answer[:-1])
