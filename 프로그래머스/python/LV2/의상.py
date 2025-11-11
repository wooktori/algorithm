def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1

    for i in dict.items():
        answer *= i[1] + 1

    return answer - 1
