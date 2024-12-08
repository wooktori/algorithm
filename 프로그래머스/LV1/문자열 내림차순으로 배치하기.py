def solution(s):
    arr = []
    for i in s:
        arr.append(i)
    arr.sort(reverse=True)
    return "".join(arr)
