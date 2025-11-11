def solution(friends, gifts):
    answer = 0
    arr = [[0] * len(friends) for _ in range(len(friends))]
    point = [0] * len(friends)
    answer = [0] * len(friends)
    for i in gifts:
        give, receive = i.split(" ")
        give_index = friends.index(give)
        receive_index = friends.index(receive)
        arr[give_index][receive_index] += 1

    for i in range(len(friends)):
        for j in range(len(friends)):
            point[i] += arr[i][j]
            point[j] -= arr[i][j]

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i > j:
                if arr[i][j] > arr[j][i]:
                    answer[i] += 1
                elif arr[i][j] < arr[j][i]:
                    answer[j] += 1
                else:
                    if point[i] > point[j]:
                        answer[i] += 1
                    elif point[i] < point[j]:
                        answer[j] += 1

    return max(answer)
