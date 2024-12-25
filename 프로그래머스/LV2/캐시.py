from collections import deque

def solution(cacheSize, cities):
    answer = 0
    arr = deque()
    for i in cities:
        city = i.lower()
        if city not in arr:
            answer += 5
            arr.append(city)
            if len(arr)>cacheSize:
                arr.popleft()
        else:
            arr.remove(city)
            arr.append(city)
            answer += 1
    return answer