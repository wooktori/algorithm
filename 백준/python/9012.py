import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    vps = input()

    for i in vps:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack):
            print("NO")
        else:
            print("YES")
