import heapq

def solution(picks, minerals):
    answer = 0
    # 최대 캘 수 있는 광물 개수 제한
    minerals = minerals[:sum(picks) * 5]
    
    # 각 곡괭이별 피로도 계산 리스트
    fatigue_list = []
    
    # 5개씩 묶어서 피로도 계산
    for i in range(0, len(minerals), 5):
        diamond_fatigue = sum(1 for m in minerals[i:i+5])
        iron_fatigue = sum(5 if m == 'diamond' else 1 for m in minerals[i:i+5])
        stone_fatigue = sum(25 if m == 'diamond' else 5 if m == 'iron' else 1 for m in minerals[i:i+5])
        
        # 돌 곡괭이 기준 피로도가 높은 순서로 정렬하기 위해 음수로 저장
        heapq.heappush(fatigue_list, (-stone_fatigue, diamond_fatigue, iron_fatigue))

    # 사용 가능한 곡괭이 리스트 (다이아 -> 철 -> 돌)
    available_picks = ([0] * picks[0]) + ([1] * picks[1]) + ([2] * picks[2])
    
    # 가장 피로도가 높은 구간부터 곡괭이 배정
    for _ in range(len(available_picks)):
        if not fatigue_list:
            break
        
        s_fatigue, d_fatigue, i_fatigue = heapq.heappop(fatigue_list)
        pick = available_picks.pop(0)  # 가장 좋은 곡괭이 사용
        
        if pick == 0:  # 다이아 곡괭이
            answer += d_fatigue
        elif pick == 1:  # 철 곡괭이
            answer += i_fatigue
        else:  # 돌 곡괭이
            answer += -s_fatigue  # stone_fatigue는 음수로 저장했으므로 부호 변경
    
    return answer
