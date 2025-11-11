from itertools import combinations


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        temp = sum(i)
        check = True
        for j in range(2, temp):
            if temp % j == 0:
                check = False
        if check == True:
            answer += 1

    return answer
