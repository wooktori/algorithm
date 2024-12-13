def solution(keymap, targets):
    answer = []
    alphabet = [101] * 26
    for i in keymap:
        for j in range(len(i)):
            if alphabet[ord(i[j])-65] > j:
                alphabet[ord(i[j])-65] = j + 1
                
    for i in targets:
        temp = 0
        for j in range(len(i)):
            num = alphabet[(ord(i[j]))-65]
            if num == 101:
                temp = -1
                break
            temp += alphabet[ord(i[j])-65]
        answer.append(temp)
    return answer