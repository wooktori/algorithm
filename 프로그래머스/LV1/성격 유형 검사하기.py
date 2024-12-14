def solution(survey, choices):
    answer = ""
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3

    arr = list(dic.items())
    for i in range(0, 8, 2):
        if arr[i][1] >= arr[i + 1][1]:
            answer += arr[i][0]
        else:
            answer += arr[i + 1][0]
    return answer
