def solution(want, number, discount):
    answer = 0

    for i in range(0, len(discount) - 9):
        check = True
        for j in range(len(want)):
            if discount[i : i + 10].count(want[j]) < number[j]:
                check = False
        if check:
            answer += 1
    return answer
