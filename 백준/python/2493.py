import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# [인덱스, 높이]의 형태로 저장
stack = []
ans = []

for i in range(N):
    while stack:
        if stack[-1][1] < arr[i]:
            stack.pop()
        else:
            ans.append(stack[-1][0] + 1)
            break

    if not stack:
        ans.append(0)
    stack.append([i, arr[i]])

for i in range(len(ans)):
    print(ans[i], end=" ")
