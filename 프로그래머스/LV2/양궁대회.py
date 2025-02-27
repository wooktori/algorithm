from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    maxV = 0
    score = [i for i in range(0, 11)]
    for i in combinations_with_replacement(score, n):
        lion = [0] * 11
        lion_score = 0
        appeach_score = 0
        # 라이언의 과녁 배열 만들기.
        for k in i:
            lion[10 - k] += 1
        # 라이언과 어피치의 배열 비교해서 점수 생성하기.
        for k in range(11):
            if info[k] < lion[k]:
                lion_score += 10 - k
            elif info[k] >= lion[k] and info[k] != 0:
                appeach_score += 10 - k

        if maxV < lion_score - appeach_score:
            answer = lion
            maxV = lion_score - appeach_score
    if maxV == 0:
        return [-1]
    return answer
