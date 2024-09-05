# 각 사분면에 따라 계산
import sys

input = sys.stdin.readline


def recursive(N, r, c, ans):
    length = 2**N / 2
    if N == 1:
        print(ans + 2 * r + c)
        return
    if length > r and length > c:
        recursive(N - 1, r, c, ans)
    elif length <= r and length > c:
        recursive(N - 1, r - 2 ** (N - 1), c, ans + 2 * 4 ** (N - 1))
    elif length > r and length <= c:
        recursive(N - 1, r, c - 2 ** (N - 1), ans + 4 ** (N - 1))
    else:
        recursive(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1), ans + 3 * 4 ** (N - 1))


N, r, c = map(int, input().split())
recursive(N, r, c, 0)
