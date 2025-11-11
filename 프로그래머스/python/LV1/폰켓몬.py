def solution(nums):
    length = len(nums) // 2
    if length < len(set(nums)):
        return length
    else:
        return len(set(nums))
