def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score) // m):
        start = i * m
        answer += m * score[start : start + m][-1]
    return answer
