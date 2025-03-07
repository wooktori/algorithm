def solution(gems):
    answer = []
    n = len(set(gems))
    dic = {}
    start = 0
    for i in range(len(gems)):
        if gems[i] in dic:
            dic[gems[i]] += 1
        else:
            dic[gems[i]] = 1
        while len(dic) == n:
            answer.append([start + 1, i + 1])
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
    answer.sort(key=lambda x: [x[1] - x[0], x[0]])
    return answer[0]
