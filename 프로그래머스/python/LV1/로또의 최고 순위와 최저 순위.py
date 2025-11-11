def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
        if i == 0:
            zero += 1
    print(correct, zero)
    answer.append(6 if 7 - (correct + zero) == 7 else 7 - (correct + zero))
    answer.append(6 if 7 - correct == 7 else 7 - correct)
    return answer
