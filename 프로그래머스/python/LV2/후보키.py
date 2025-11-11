from itertools import combinations


def solution(relation):
    candidates = []
    col = len(relation[0])

    # combination을 이용해 전체 경우의 수 저장.
    for i in range(1, col + 1):
        candidates.extend(list(combinations(range(col), i)))

    answer = []
    for c in candidates:
        temp = []
        for i in relation:
            temp.append(tuple(i[j] for j in c))

        if len(set(temp)) == len(relation):
            flag = False
            for u in answer:
                if set(u).issubset(set(c)):
                    flag = True
                    break
            if flag == False:
                answer.append(c)

    return len(answer)
