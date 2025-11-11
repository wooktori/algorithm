def solution(fees, records):
    answer = {
        i: fees[1] for i in set([i[6:10] for i in records])
    }  # <차량번호 : 기본요금> 을 키와 값으로 갖는 딕셔너리 생성.
    sorted_answer = dict(sorted(answer.items()))  # 차량번호를 기준으로 정렬.
    dic = {}  # <차량번호 : 누적 주차 시간> 을 키와 값으로 갖는 딕셔너리.

    # 총 누적시간 담기.
    for i in records:
        time = int(i[:2]) * 60 + int(
            i[3:5]
        )  # 입/출차 기록에서 시각의 위치는 항상 일정. 해당 인덱스를 분으로 변환해서 변수에 할당.
        car_num = i[6:10]
        if i[-2:] == "IN":  # 입차일 경우
            if car_num in dic:  # 이미 값이 존재하는 경우와 아닌 경우.
                dic[car_num] -= time
            else:
                dic[car_num] = -time
        else:  # 출차일 경우
            dic[car_num] += time

    # 입차 기록만 있고 출차 기록은 없는 예외 처리.
    for i in dic:
        if dic[i] <= 0:
            dic[i] += 1439

    # 누적 시간을 바탕으로 금액 계산.
    for i in dic:
        a_time = dic[i] - fees[0]  # 누적 시간에서 기본 시간을 제외한 추가 시간.
        if a_time > 0:
            if a_time % fees[2] == 0:
                sorted_answer[i] += (dic[i] - fees[0]) // fees[2] * fees[3]
            else:
                sorted_answer[i] += ((dic[i] - fees[0]) // fees[2] + 1) * fees[3]

    return [sorted_answer[i] for i in sorted_answer]
