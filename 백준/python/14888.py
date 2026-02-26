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

#11/15
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
maxV = int(-1e9)
minV = int(1e9)

def dfs(i, now):
    global plus, minus, mul, div, maxV, minV
    if i == N:
        maxV = max(maxV, now)
        minV = min(minV, now)
        return
    
    else:
        if plus>0:
            plus-=1
            dfs(i+1, now + nums[i])
            plus+=1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - nums[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / nums[i]))
            div += 1
        

dfs(1,nums[0])
print(maxV)
print(minV)