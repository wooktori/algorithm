def solution(skill, skill_trees):
    answer = 0
    arr = []
    for i in skill_trees:
        temp = ""
        for j in i:
            if j in skill:
                temp += j
        arr.append(temp)

    for i in range(len(skill)):
        for j in arr:
            if j == skill[: len(skill) - i]:
                answer += 1

    for i in arr:
        if i == "":
            answer += 1
    return answer
