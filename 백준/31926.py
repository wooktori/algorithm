import sys

input = sys.stdin.readline


N = int(input())

for i in range(30):
    if 2**i <= N < 2 ** (i + 1):
        print(10 + i)
