def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    wordX = ["ayaaya", "yeye", "woowoo", "mama"]
    for i in babbling:
        for j in wordX:
            if j in i:
                i = i.replace(j, "x")
        for j in word:
            if j in i:
                i = i.replace(j, " ")

        i = i.replace(" ", "")
        if i == "":
            answer += 1

    return answer
