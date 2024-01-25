import sys


def Input_Data():
    N = int(sys.stdin.readline())
    list_meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    return N, list_meeting


# 입력받는 부분
N, list_meeting = Input_Data()

# 여기서부터 작성
meeting_dict = {idx+1: meeting[1:] for idx, meeting in enumerate(list_meeting)}

list_meeting.sort(key=lambda x: (x[1], x[2]))
answer = [list_meeting[0][0]]

for meeting in list_meeting[1:]:
    cur_meeting_num, cur_meeting_start, cur_meeting_end = meeting
    prev_meeting_start, prev_meeting_end = meeting_dict[answer[-1]]

    # 미팅 시간이 겹치면
    if prev_meeting_end > cur_meeting_start:
        if prev_meeting_end <= cur_meeting_end:
            pass
        else:
            answer[-1] = cur_meeting_num
    else:
        answer.append(cur_meeting_num)

# 출력하는 부분
print(len(answer))
print(*answer)
