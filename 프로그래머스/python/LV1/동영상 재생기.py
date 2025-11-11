# commands를 순회하며 원소에 맞게 타임라인 이동
# 1. 현재 시간값과 오프닝 시간 체크 => 사이값일 경우 오프닝 끝나는 시간 이동
# 2. next, prev에 맞게 10초 전후로 이동
def solution(video_len, pos, op_start, op_end, commands):
    answer = ""
    total_s, total_e = video_len.split(":")
    op_s_s, op_s_e = op_start.split(":")
    op_e_s, op_e_e = op_end.split(":")
    present_s, present_e = pos.split(":")

    total_video = int(total_s) * 60 + int(total_e)
    present = int(present_s) * 60 + int(present_e)
    op_s = int(op_s_s) * 60 + int(op_s_e)
    op_e = int(op_e_s) * 60 + int(op_e_e)

    if op_s <= present < op_e:
        present = op_e

    for i in commands:
        if op_s <= present < op_e:
            present = op_e

        if i == "next":
            present += 10
            if present > total_video:
                present = total_video
        else:
            present -= 10
            if present < 0:
                present = 0

    if op_s <= present < op_e:
        present = op_e

    answer += (
        "0" + str(present // 60) if len(str(present // 60)) == 1 else str(present // 60)
    )
    answer += ":"
    answer += (
        "0" + str(present % 60) if len(str(present % 60)) == 1 else str(present % 60)
    )
    return answer
