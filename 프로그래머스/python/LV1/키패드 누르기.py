def solution(numbers, hand):
    answer = ""
    arr = [
        [3, 1],
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 0],
        [2, 1],
        [2, 2],
        [3, 0],
        [3, 2],
    ]
    left_position = 10
    right_position = 11
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            left_position = i
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            right_position = i
        else:
            left_dis = abs(arr[i][0] - arr[left_position][0]) + abs(
                arr[i][1] - arr[left_position][1]
            )
            right_dis = abs(arr[i][0] - arr[right_position][0]) + abs(
                arr[i][1] - arr[right_position][1]
            )
            if left_dis > right_dis:
                answer += "R"
                right_position = i
            elif left_dis < right_dis:
                answer += "L"
                left_position = i
            else:
                if hand == "right":
                    answer += "R"
                    right_position = i
                else:
                    answer += "L"
                    left_position = i

    return answer
