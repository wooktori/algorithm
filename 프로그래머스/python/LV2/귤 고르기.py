def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    sorted_dic = dict(sorted(dic.items(), key=lambda x: -x[1]))

    for i in sorted_dic:
        if k <= 0:
            continue
        k -= sorted_dic[i]
        answer += 1
    return answer
