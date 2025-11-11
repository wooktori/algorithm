import math


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        temp = yak(i, limit)
        if temp > limit:
            answer += power
        else:
            answer += temp
    return answer


def yak(n, limit):
    ans = 0
    for i in range(1, int(math.sqrt(n + 1)) + 1):
        if n % i == 0:
            ans += 1
            if i < n // i:
                ans += 1
        if ans > limit:
            break
    return ans
