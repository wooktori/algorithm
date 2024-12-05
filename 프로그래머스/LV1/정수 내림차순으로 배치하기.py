def solution(n):
    list = [i for i in str(n)]
    list.sort(reverse=True)

    return int("".join(list))
