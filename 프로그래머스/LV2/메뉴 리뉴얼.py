from itertools import combinations


def solution(orders, course):
    answer = []

    for i in course:
        dic = {}
        order_combinations = []

        for order in orders:
            temp = combinations(list(order), i)  # order에서 i개만큼의 조합 생성

            for j in temp:  # 딕셔너리에 만들어진 문자열 삽입
                str = "".join(sorted(j))

                if dic.get(str):
                    dic[str] += 1

                else:
                    dic[str] = 1

        # 최댓값 임시배열에 저장 후 정답배열에 추가
        arr = [k for k, v in dic.items() if ((v == max(dic.values())) and v >= 2)]
        answer += arr

    return sorted(answer)
