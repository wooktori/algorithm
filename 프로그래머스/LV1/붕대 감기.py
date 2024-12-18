def solution(bandage, health, attacks):
    answer = health
    seq = 0
    time = attacks[-1][0]
    attacked = False
    
    for i in range(1, time+1):
        for j in attacks:
            if i == j[0]:
                answer -= j[1]
                seq = 0
                attacked = True
                break
        if attacked :
            attacked = False
            continue
        seq += 1

        if seq == bandage[0]:
            answer += bandage[2]
            seq = 0
        
        answer += bandage[1]
        if answer > health:
            answer = health
        if answer <= 0:
            return -1
    if answer <= 0:
        return -1
    return answer