def solution(n, words):
    answer = []
    used = []
    for i in range(len(words)):
        if i > 0 and used[-1][-1] != words[i][0]:
            answer.append(i % n + 1)
            answer.append(((i + 1 - answer[0]) // n) + 1)
            break

        if words[i] not in used:
            used.append(words[i])
        else:
            answer.append(i % n + 1)
            answer.append(((i + 1 - answer[0]) // n) + 1)
            break

    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    return answer
