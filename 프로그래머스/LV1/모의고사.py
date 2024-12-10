def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    t1 = 0
    t2 = 0
    t3 = 0

    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            t1 += 1
        if answers[i] == second[i % 8]:
            t2 += 1
        if answers[i] == third[i % 10]:
            t3 += 1
    answer = [t1, t2, t3]
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)
    return sorted(result)
