def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])
        string = ""
        for i in temp[2:]:
            if i == "1":
                string += "#"
            else:
                string += " "
        if len(string) < n:
            string = " " * (n - len(string)) + string
        answer.append(string)
    return answer
