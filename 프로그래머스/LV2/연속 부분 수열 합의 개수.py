def solution(elements):
    answer = []
    double = elements * 2
    for i in range(len(double)):
        for j in range(len(elements)):
            answer.append(sum(double[i : i + j + 1]))
    return len(list(set(answer)))
