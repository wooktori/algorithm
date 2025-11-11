def solution(data, ext, val_ext, sort_by):
    answer = []
    arr = ["code", "date", "maximum", "remain"]

    for i in data:
        index = arr.index(ext)
        if i[index] < val_ext:
            answer.append(i)

    sort_index = arr.index(sort_by)
    answer.sort(key=lambda x: x[sort_index])
    return answer
