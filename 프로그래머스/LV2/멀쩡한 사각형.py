import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


# 시간초과
# def solution(w,h):
#     answer = w*h
#     for i in range(h):
#         for j in range(w):
#             if -w < w*i - h*j < h:
#                 answer -= 1
#     return answer
