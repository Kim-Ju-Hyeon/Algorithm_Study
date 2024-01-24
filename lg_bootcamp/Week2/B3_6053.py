import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    words = readl().split()
    return N, words

# 입력받는 부분
N, words = Input_Data()

# 여기서부터 작성
def Solve():
    word_dict = {}
    unique = True
    for idx, word in enumerate(words):
        if word not in word_dict:
            word_dict[word] = [idx+1]
        else:
            word_dict[word].append(idx+1)
            unique = False

    if unique:
        print("unique")
    else:
        for word in word_dict:
            if len(word_dict[word]) == 1:
                continue
            print(word, end=' ')
            print(*word_dict[word])

Solve()