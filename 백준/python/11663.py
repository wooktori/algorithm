import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()


def min_dot(a):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if a > dots[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def max_dot(a):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if a >= dots[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end


for i in range(M):
    a, b = map(int, input().split())
    print(max_dot(b) - min_dot(a) + 1)
