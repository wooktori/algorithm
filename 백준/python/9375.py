import sys

input = sys.stdin.readline


def sol():
    n = int(input())
    dict = {}
    ans = 1
    for _ in range(n):
        cloth, category = input().split()
        if category in dict:
            dict[category].append(cloth)
        else:
            dict[category] = [cloth]
    for i in dict:
        ans *= len(dict[i]) + 1
    print(ans - 1)


t = int(input())
for _ in range(t):
    sol()
