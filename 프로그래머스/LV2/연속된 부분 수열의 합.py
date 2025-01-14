def solution(sequence, k):
    answer = []
    start, end = 0, 0
    total = sequence[0]

    while True:
        if total == k:
            if len(answer) == 0:
                answer.append(start)
                answer.append(end)
            elif answer[1] - answer[0] > end - start:
                answer.pop()
                answer.pop()
                answer.append(start)
                answer.append(end)
            total -= sequence[start]
            start += 1

        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            end += 1
            if end == len(sequence):
                break
            total += sequence[end]

    return answer
