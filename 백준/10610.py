import sys

input = sys.stdin.readline

n = input().rstrip()
sum = 0


if "0" not in n:
    print(-1)
else:
    for i in range(len(n)):
        sum += int(n[i])

    if sum % 3 == 0:
        print("".join(sorted(n, reverse=True)))
    else:
        print(-1)
