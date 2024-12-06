def solution(s):
    answer = ""
    arr = s.split(" ")
    for i in range(len(arr)):
        temp = list(arr[i])
        for j in range(len(temp)):
            if j % 2 == 0:
                temp[j] = temp[j].upper()
            else:
                temp[j] = temp[j].lower()
        arr[i] = "".join(temp)

    return " ".join(arr)
