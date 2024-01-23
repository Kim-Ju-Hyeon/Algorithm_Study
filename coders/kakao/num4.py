import sys

def solution(coin, cards):
    n = 2 * max(cards)  # n은 카드 뭉치에 있는 카드 중 최대 숫자의 두 배
    max_rounds = 0  # 가능한 최대 라운드 수

    # cards 배열은 시작할 때 가지고 있는 카드들을 나타냄
    # 가능한 모든 카드 조합을 고려
    card_pool = list(range(1, n + 1))

    stack = [(cards, coin, 0)]  # 스택에 초기 상태 추가

    while stack:
        current_cards, remaining_coins, rounds = stack.pop()

        if len(current_cards) < 2:
            max_rounds = max(max_rounds, rounds)
            continue

        # 라운드마다 두 장의 카드를 뽑음
        for i in range(len(card_pool)):
            for j in range(i + 1, len(card_pool)):
                drawn_cards = [card_pool[i], card_pool[j]]

                # 동전을 사용하여 카드를 가지는 경우
                if remaining_coins > 0:
                    new_cards = current_cards + drawn_cards
                    new_rounds = rounds
                    if sum(drawn_cards) == n + 1:
                        new_rounds += 1
                    stack.append((new_cards, remaining_coins - 1, new_rounds))

                # 동전을 사용하지 않고 버리는 경우
                stack.append((current_cards, remaining_coins, rounds))

    return max_rounds

# 테스트
coin = 4  # 예시 동전 수
cards = [3, 6, 7, 2]  # 예시 카드
print(solution(coin, cards))  # 최대 라운드 수 출력