def bigN(k):
    if k == 1:
        return 0
    temp = [1]
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0 and i <= 10000000:
            temp.append(i)
            if k // i <= 10000000:
                temp.append(k // i)
    return max(temp)


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(bigN(i))
    return answer
