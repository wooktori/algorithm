def solution(s):
    half = len(s) // 2
    if len(s) % 2 == 0:
        return s[half - 1 : half + 1]
    else:
        return s[half]
