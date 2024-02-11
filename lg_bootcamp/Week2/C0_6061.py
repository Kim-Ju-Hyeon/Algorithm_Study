import sys

def Input_Data():
    N = int(sys.stdin.readline())
    list_time = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    return N, list_time

# 입력받는 부분
N, list_time = Input_Data()

# 여기서부터 작성
def solution():
    list_time.sort()

    library_use_time = [list_time[0]]
    for cur_in, cur_out in list_time[1:]:
        prev_in, prev_out = library_use_time[-1]

        if prev_out >= cur_in:
            library_use_time[-1][1] = max(prev_out, cur_out)
        else:
            library_use_time.append([cur_in, cur_out])

    answer = [-1, -1]
    for idx, use_list in enumerate(library_use_time):
        used_duration = use_list[1] - use_list[0]
        answer[0] = max(answer[0], used_duration)

        if idx > 0:
            no_one_duration = library_use_time[idx][0] - library_use_time[idx-1][1]
            answer[1] = max(answer[1], no_one_duration)
    return answer

print(*solution())