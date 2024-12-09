def solution(k, score):
    answer = []
    goat = []

    for i in range(len(score)):
        goat.append(score[i])
        goat.sort(reverse=True)

        if len(goat) > k:
            goat.pop()

        answer.append(goat[-1])

    return answer
