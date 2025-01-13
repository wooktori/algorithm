def solution(numbers, target):
    answers = [0]
    answer = 0

    for number in numbers:
        arr = []
        for i in answers:
            arr.append(i + number)
            arr.append(i - number)
        answers = arr

    for i in answers:
        if i == target:
            answer += 1
    return answer
