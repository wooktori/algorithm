import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
lastBook = 0
ans = 0
positiveArr = []
negativeArr = []

# 양수/음수 배열로 각각 나누고 마지막에 배달할 책 거리 저장
for i in range(len(arr)):
    if abs(arr[i]) > lastBook:
        lastBook = abs(arr[i])
    if arr[i] > 0:
        positiveArr.append(arr[i])
    else:
        negativeArr.append(arr[i])

# 각 배열을 정렬
positiveArr.sort(reverse=True)
negativeArr.sort()

# M개의 책에서 가장 멀리있는 책의 거리 * 2를 정답에 더해주기
for i in range(0, len(positiveArr), M):
    ans += 2 * positiveArr[i]
for i in range(0, len(negativeArr), M):
    ans += 2 * abs(negativeArr[i])

# 돌아오지 않아도 되기 때문에 가장 멀리 있는 책 값 빼주기
print(ans - lastBook)
