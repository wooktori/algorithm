def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    arr = []
    for i in range(len(routes)):
        for j in arr:
            if routes[i][0] <= j <= routes[i][1]:
                break
        else:
            answer += 1
            arr.append(routes[i][1])
    return answer
