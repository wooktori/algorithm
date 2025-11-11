def solution(record):
    answer = []
    dic = {}
    for i in record:
        temp = i.split(" ")
        if temp[0] == "Enter":
            dic[temp[1]] = temp[2]
            answer.append(temp[1] + "  님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(temp[1] + "  님이 나갔습니다.")
        else:
            dic[temp[1]] = temp[2]
    for i in range(len(answer)):
        temp = answer[i].split("  ")
        answer[i] = dic[temp[0]] + temp[1]
    return answer
