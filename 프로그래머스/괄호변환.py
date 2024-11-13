def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
def correct(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if len(p)==0:
        return answer
    
    index = balance(p)
    u = p[:index+1]
    v = p[index+1:]

    if correct(u):
        answer = u + solution(v)
    else:
        temp = "(" + solution(v) + ")"
        u = u[1:-1]
        for i in u:
            if i=="(":
                temp += ")"
            else:
                temp += "("
        answer = temp
    return answer