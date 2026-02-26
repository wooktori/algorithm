import sys

input = sys.stdin.readline

N = int(input())
stack = []
ans = []
temp = 1
flag = False

for _ in range(N):
    num = int(input())
    while temp <= num:
        stack.append(temp)
        ans.append("+")
        temp += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        flag = True

if flag:
    print("NO")
else:
    for i in ans:
        print(i)
