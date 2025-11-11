def solution(dartResult):
    answer = 0
    temp = ""
    list = []
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i == "S":
            temp = int(temp) ** 1
            list.append(temp)
            temp = ""
        elif i == "D":
            temp = int(temp) ** 2
            list.append(temp)
            temp = ""
        elif i == "T":
            temp = int(temp) ** 3
            list.append(temp)
            temp = ""
        elif i == "*":
            if len(list) > 1:
                list[-2] = 2 * list[-2]
                list[-1] = 2 * list[-1]
            else:
                list[-1] = 2 * list[-1]

        else:
            list[-1] = -1 * list[-1]

    return sum(list)
