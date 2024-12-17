def check(today, year, month, day):
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:10])
    if today_year > year:
        return True
    elif today_year == year:
        if today_month > month:
            return True
        elif today_month == month:
            if today_day > day:
                return True
            return False
        return False
    return False


def solution(today, terms, privacies):
    answer = []
    for i in range(len(privacies)):
        year = int(privacies[i][:4])
        month = int(privacies[i][5:7])
        day = int(privacies[i][8:10])
        for j in terms:
            if privacies[i][-1] in j:
                time = int(j[2:])
                day -= 1
                if day == 0:
                    day = 28
                    month -= 1
                month += time
                if month > 12:
                    if month % 12 == 0:
                        year += (month // 12) - 1
                        month = 12
                    else:
                        year += month // 12
                        month = month % 12

        if check(today, year, month, day):
            answer.append(i + 1)

    return answer
