def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = {i: 0 for i in enroll}
    answer["minho"] = 0

    dic = {}

    for i in range(n):
        if referral[i] == "-":
            dic[enroll[i]] = "minho"
        else:
            dic[enroll[i]] = referral[i]

    for i in range(len(seller)):
        value = amount[i] * 100
        node = seller[i]

        while node != "minho" and value > 0:
            tax = value // 10
            answer[node] += value - tax
            value = tax
            node = dic[node]

    return list(answer.values())[:-1]
