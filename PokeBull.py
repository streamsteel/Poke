# 扑克牌斗牛
from Poke import cards
import random
from itertools import combinations
import time


card_change = {
    11: 'J',
    12: 'Q',
    13: 'K',
    1 : 'A',
}

class Bull():
    # 斗牛类
    def __init__(self, cards):
        self.cards = cards  # 玩家手牌
        self.tail = ''
    
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
            if sum(copy_card) % 10 == 0 and len([_c for _c in copy_card if _c >= 10])>=2:
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
                    self.tail = str(sum(copy_card_2) % 10)
                    return True
        

                

card = cards()
print('原始牌组:', card.allcards)
card.shuffle_card()  # 洗牌
print('洗牌后:', card.allcards)
print('游戏开始'.center(50, '='))


while True:
    # 抽五张牌
    mycard = card.take_card(5)
    showcard = []
    for _card in mycard:
        if _card in card_change.keys():
            showcard.append(card_change[_card])
        else:
            showcard.append(_card)
    print('手牌:', showcard)

    # 判断是否有牛
    bull = Bull(mycard)
    if bull.isBoom():
        print('You have a fucking Boom!!!')
    elif bull.islessTen():
        print('You are lessTen!')
    elif bull.isGold():
        print('You have a uplifting Glod-Bull!!!')
    elif bull.isExBull():
        print('You have the Bull - ' + bull.tail)
    else:
        print('You are unlucky,you have nothing but me~')

    # 洗牌重新开始
    card.recovery()
    time.sleep(5)
    print('游戏开始'.center(50, '='))