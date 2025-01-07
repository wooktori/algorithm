def solution(fees, records):
    answer = {i: fees[1] for i in set([i[6:10] for i in records])}
    sorted_answer = dict(sorted(answer.items()))
    dic = {}
    for i in records:
        time = int(i[:2]) * 60 + int(i[3:5])
        if i[-2:] == "IN":
            if i[6:10] in dic:
                dic[i[6:10]] -= time
            else:
                dic[i[6:10]] = -time
        else:
            dic[i[6:10]] += time

    for i in dic:
        if dic[i] <= 0:
            dic[i] += 1439

    for i in dic:
        a_time = dic[i] - fees[0]
        if a_time > 0:
            if a_time % fees[2] == 0:
                sorted_answer[i] += (dic[i] - fees[0]) // fees[2] * fees[3]
            else:
                sorted_answer[i] += ((dic[i] - fees[0]) // fees[2] + 1) * fees[3]

    return [sorted_answer[i] for i in sorted_answer]
