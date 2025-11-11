def solution(plans):
    answer = []
    stack = []
    # plans 데이터 변형
    for i in range(len(plans)):    
        plans[i][1] = int(plans[i][1][:2])*60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]]) # [name, playtime]
        gap = plans[i+1][1] - plans[i][1]
        
        while stack and gap:
            if stack[-1][1] <= gap:
                name, time = stack.pop()
                gap -= time
                answer.append(name)
            else:
                stack[-1][1] -= gap
                gap = 0
                
    answer.append(plans[-1][0]) # 마지막 과제 append
    
    for i in range(len(stack)):
        answer.append(stack[~i][0]) # 역순으로 append
    return answer
