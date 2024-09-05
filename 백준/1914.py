import sys

input = sys.stdin.readline


def hanoi(n, first, second, third):
    if n == 1:
        print(first, third)
        return
    hanoi(n - 1, first, third, second)
    print(first, third)
    hanoi(n - 1, second, first, third)


n = int(input())
print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)
