def solution(s):
    answer = []
    arr = list(s.split(" "))
    for i in arr:
        answer.append(i.capitalize())
    return " ".join(answer)
