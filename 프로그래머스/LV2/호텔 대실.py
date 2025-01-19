import heapq

def change_time(time):
    h, m = map(int, time.split(":"))
    return h*60+m

def solution(book_time):
    answer = 0
    q = []
    book_time.sort(key=lambda x:x[0])

    for start, end in book_time:
        start_time = change_time(start)
        end_time = change_time(end) + 10
        
        if q and start_time >= q[0]:
            heapq.heappop(q)
        else:
            answer += 1
        
        heapq.heappush(q, end_time)
        
        
    return answer