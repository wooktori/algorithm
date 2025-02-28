def solution(n, s):
    answer = []
    if n > s:
        answer = [-1]
    else:
        for _ in range(n):
            answer.append(s // n)
        d = s % n
        for i in range(d):
            answer[i] += 1

        answer.sort()

    return answer
