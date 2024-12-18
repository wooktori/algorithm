def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dict = {x:0 for x in id_list}
    report = list(set(report))
    
    for i in report:
        a, b = i.split()
        dict[b] += 1    
    
    for i in report:
        a, b = i.split()
        if dict[b] >= k:
            answer[id_list.index(a)] += 1
        
    return answer