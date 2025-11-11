def solution(name):
    answer = 0
    minV = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        minV = min(minV, i * 2 + len(name) - next, i + 2 * (len(name) - next))

    return answer + minV
