def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    y = 0
    for start, end in targets:
        if start >= y:
            answer += 1
            y = end
    return answer
