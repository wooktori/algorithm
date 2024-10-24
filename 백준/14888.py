import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
maxV = -1e9
minV = 1e9


def func(plus, minus, mul, div, count, sum):
    global maxV, minV
    if count == N:
        maxV = max(maxV, sum)
        minV = min(minV, sum)
        return

    if plus:
        func(plus - 1, minus, mul, div, count + 1, sum + nums[count])
    if minus:
        func(plus, minus - 1, mul, div, count + 1, sum - nums[count])
    if mul:
        func(plus, minus, mul - 1, div, count + 1, sum * nums[count])
    if div:
        func(plus, minus, mul, div - 1, count + 1, int(sum / nums[count]))


func(plus, minus, mul, div, 1, nums[0])
print(maxV)
print(minV)
