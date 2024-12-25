def solution(s):
    answer = []
    s = s[2:-2]
    arr = s.split("},{")
    arr.sort(key=len)
    for i in arr:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
