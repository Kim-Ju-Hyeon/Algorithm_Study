import sys

def input_data():
    readl = sys.stdin.readline
    N, str_org = readl().split()
    return int(N), str_org

sol = []

# 입력받는 부분
N, str_org = input_data()

# 여기서부터 작성
def solution():
    tree = {0: [int(str_org[0])]}
    level = 0
    spy_num = ''

    for char in str_org[1:]:
        if char == '<':
            if spy_num == '':
                level += 1
                continue
            else:
                spy_num = int(spy_num)

            if level in tree:
                tree[level] += [spy_num]
            else:
                tree[level] = [spy_num]

            level += 1
            spy_num = ''


        elif char == '>':
            if spy_num == '':
                level -= 1
                continue
            else:
                spy_num = int(spy_num)

            if level in tree:
                tree[level] += [spy_num]
            else:
                tree[level] = [spy_num]

            level -= 1
            spy_num = ''
        else:
            spy_num += char


    return tree


print(solution())