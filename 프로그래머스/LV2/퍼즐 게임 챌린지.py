def solution(diffs, times, limit):
    answer = 0
    start_level = 1
    end_level = max(diffs)

    while start_level <= end_level:
        level = (start_level + end_level) // 2
        total_time = 0
        for i in range(len(diffs)):
            temp = diffs[i] - level
            total_time += times[i]
            if temp > 0:
                total_time += (times[i - 1] + times[i]) * temp

        if total_time <= limit:
            end_level = level - 1
            answer = level
        else:
            start_level = level + 1
    return answer
