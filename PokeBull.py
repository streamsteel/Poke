# 扑克牌斗牛
from Poke import Cards
import random
from itertools import combinations
import time


card_change = {
    11: "J",
    12: "Q",
    13: "K",
    1: "A",
}


class Bull:
    # 斗牛类
    def __init__(self, cards):
        self.cards = cards  # 玩家手牌
        self.tail = 0       # 牛的尾数

    def isBoom(self):
        _comb_list = list(combinations(self.cards, 4))
        for comb in _comb_list:
            if len(set(comb)) == 1:
                return True

    def islessTen(self):
        if sum(self.cards) < 10:
            return True

    def isGold(self):
        if all(card >= 10 for card in self.cards):
            return True
        else:
            copy_card = []
            for card in self.cards:
                if card >= 10:
                    copy_card.append(10)
                else:
                    copy_card.append(card)
            if (
                sum(copy_card) % 10 == 0
                and len([_c for _c in copy_card if _c >= 10]) >= 2
            ):
                return True

    def isExBull(self):
        if len(list(card for card in self.cards if card >= 10)) >= 3:
            self.tail = str(sum([card for card in self.cards if card <= 10]) % 10)
            return True
        else:
            copy_card = []
            for card in self.cards:
                if card >= 10:
                    copy_card.append(10)
                else:
                    copy_card.append(card)
            _comb_list = list(combinations(copy_card, 3))
            for comb in _comb_list:
                copy_card_2 = copy_card
                if sum(comb) % 10 == 0:
                    for c in comb:
                        copy_card_2.remove(c)
                    print(copy_card_2)
                    self.tail = sum(copy_card_2) % 10
                    return True


def game(n: int = 2):
    # n : 玩家人数
    # 生成一副扑克牌
    cards = Cards()
    print("洗牌中...")
    time.sleep(1)
    cards.shuffle_card()  # 洗牌
    # 发牌
    player_cards = []
    for _ in range(n):
        player_cards.append(cards.take_card(5))
    # 玩家手牌
    player_cards = [Bull(player_card) for player_card in player_cards]
    # 玩家手牌排序
    player_cards = sorted(player_cards, key=lambda x: x.cards, reverse=True)
    # 玩家手牌展示
    for i, player_card in enumerate(player_cards):
        print(f"玩家{i+1}的手牌为：", end="")
        for card in player_card.cards:
            print(card_change.get(card, card), end=" ")
        print()
    # 判断玩家手牌
    winner = {k: 0 for k in range(n)}
    for i, player_card in enumerate(player_cards):
        if player_card.isBoom():
            print(f"Player{i+1}: 炸弹")
            winner[i] = 999
        elif player_card.islessTen():
            print(f"Player{i+1}: 10小")
            winner[i] = 998
        elif player_card.isGold():
            print(f"Player{i+1}: 满牛")
            winner[i] = 997
        elif player_card.isExBull():
            print(f"Player{i+1}: 牛{player_card.tail}")
            winner[i] = player_card.tail + 500
        else:
            print(f"Player{i+1}: 没牛")
            winner[i] = max(player_card.cards)

    # 判断胜负: 999 > 998 > 997 > 500 > 499 > ... > 0, 输出胜利者key
    winner = sorted(winner.items(), key=lambda x: x[1], reverse=True)
    print(f"胜利者为：|-*- Player{winner[0][0]+1} -*-|")
    print("游戏结束")


if __name__ == "__main__":
    card = Cards()
    print("游戏开始".center(50, "="))

    while True:
        # Ctrl + C 退出 Signal
        try:
            game()
            # 洗牌重新开始
            input("按Enter开始下一把\n")
            card.recovery()
            print("游戏开始".center(50, "="))
        except KeyboardInterrupt:
            print("\nBye~")
            break


