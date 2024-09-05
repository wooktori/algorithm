import sys

input = sys.stdin.readline


def sol():
    a, b = map(int, input().split())
    while True:
        if a > b:
            a = a // 2
        elif a < b:
            b = b // 2
        else:
            print(a * 10)
            break


t = int(input())

for _ in range(t):
    sol()
