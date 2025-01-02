from collections import Counter


def solution(topping):
    answer = 0
    counter = Counter(topping)
    counter2 = set()

    for i in topping:
        counter[i] -= 1
        counter2.add(i)

        if counter[i] == 0:
            counter.pop(i)

        if len(counter) == len(counter2):
            answer += 1
    return answer
