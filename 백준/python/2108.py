import sys

input = sys.stdin.readline


def first(arr):
    sum = 0
    for i in arr:
        sum += i
    return round(sum / n)


def second(arr):
    arr.sort()
    return arr[len(arr) // 2]


def third(arr):
    dict = {}
    for a in arr:
        if a not in dict:
            dict[a] = 1
        else:
            dict[a] += 1
    maxV = max(dict.values())
    max_arr = sorted([k for k, v in dict.items() if v == maxV])
    if len(max_arr) > 1:
        return max_arr[1]
    else:
        return max_arr[0]


def fourth(arr):
    maxV = max(arr)
    minV = min(arr)
    return maxV - minV


n = int(input())
arr = [int(input()) for _ in range(n)]

print(first(arr))
print(second(arr))
print(third(arr))
print(fourth(arr))
