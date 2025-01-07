def solution(files):
    answer = []

    for file in files:
        head, number, tail = "", "", ""
        flag = False  # flag를 이용해 세 부분 나누기.

        for i in range(len(file)):
            if (
                flag == True and file[i].isdigit() == False
            ):  # number 구간이 지나고 나온 바로 다음 문자부터 끝까지 tail에 추가.
                tail = file[i:]
                break
            if file[i].isdigit() == False:  # 숫자가 아니라면 head에 추가.
                head += file[i]
            else:  # 숫자라면 number에 추가.
                flag = True  # flag 값을 True로 바꿔 tail을 구분할 수 있도록 함.
                number += file[i]

        answer.append([head, number, tail])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))  # 문제의 조건에 맞게 sort.

    arr = []
    for i in answer:
        temp = ""
        for j in i:
            temp += j
        arr.append(temp)

    return arr
