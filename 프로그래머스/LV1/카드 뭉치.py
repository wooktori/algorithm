def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0

    for i in range(len(goal)):
        print(i, index1, index2)
        if index1 < len(cards1):
            if goal[i] == cards1[index1]:
                index1 += 1
                continue
        if index2 < len(cards2):
            if goal[i] == cards2[index2]:
                index2 += 1
                continue

    if index1 + index2 == len(goal):
        return "Yes"
    else:
        return "No"
