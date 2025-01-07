def solution(files):
    answer = []
    for file in files:
        head, number, tail = "", "", ""
        flag = False
        for i in range(len(file)):
            if flag == True and file[i].isdigit() == False:
                tail = file[i:]
                break
            if file[i].isdigit() == False:
                head += file[i]
            else:
                flag = True
                number += file[i]

        answer.append([head, number, tail])
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    arr = []
    for i in answer:
        temp = ""
        for j in i:
            temp += j
        arr.append(temp)
    return arr
