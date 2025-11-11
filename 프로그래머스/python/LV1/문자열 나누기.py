def solution(s):
    answer = 0
    count_x = 0
    count_o = 0
    for i in s:
        if count_x == count_o:
            answer += 1
            k = i
        if k == i:
            count_x += 1
        else:
            count_o += 1

    return answer
