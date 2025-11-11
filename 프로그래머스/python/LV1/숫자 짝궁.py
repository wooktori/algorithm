def solution(X, Y):
    answer = []
    for i in range(10):
        if str(i) in X and str(i) in Y:
            maxV = min(X.count(str(i)), Y.count(str(i)))
            for j in range(maxV):
                answer.append(str(i))
    answer.sort(reverse=True)

    if len(answer) == 0:
        return "-1"
    else:
        if len(answer) == answer.count("0"):
            return "0"
        else:
            return "".join(answer)
