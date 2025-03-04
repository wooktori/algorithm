def solution(genres, plays):
    answer = []
    n = len(genres)
    dic = {}
    info = {}
    for i in range(n):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            info[genres[i]].append([i, plays[i]])
        else:
            dic[genres[i]] = plays[i]
            info[genres[i]] = [[i, plays[i]]]
    s_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    s_info = {
        key: sorted(value, key=lambda x: x[1], reverse=True)
        for key, value in info.items()
    }

    for i in s_dic:
        if len(s_info[i]) == 1:
            answer.append(s_info[i][0][0])
            continue
        for j in range(2):
            answer.append(s_info[i][j][0])
    return answer
