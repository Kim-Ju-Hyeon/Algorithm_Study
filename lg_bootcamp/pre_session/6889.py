import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


# 입력 받는 부분
N, M = Input_Data()

# M = 1
def dice_1(n):
    if n == N:
        print(*dice)
        return

    for i in range(1, 7):
        dice[n] = i
        dice_1(n+1)

def dice_2():
    pass


def dice_3():
    pass


dice = [0] * N
if M == 1:
    dice_1(0)

elif M == 2:
    dice_2()

else:
    dice_3()
