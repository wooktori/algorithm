from itertools import product

def solution(users, emoticons):
    answer = []
    discount_arr = list(product([10,20,30,40], repeat=len(emoticons)))
    
    for discount in discount_arr:
        plus = 0
        total = 0
        
        for user in users:
            percent, user_limit = user
            user_price = 0
            temp = 0
            for i in range(len(emoticons)):
                if discount[i] >= percent:
                    user_price += emoticons[i] * (100-discount[i]) // 100
                if user_price >= user_limit:
                    temp += 1
                    break
            if temp == 1:
                plus += 1
            else:
                total += user_price
        answer.append([plus, total])
    answer.sort(key=lambda x:(-x[0],-x[1]))
    
    return answer[0]    
