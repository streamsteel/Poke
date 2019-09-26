import random
class cards:
    def __init__(self, havaJoker=False):
        # 生成一副扑克牌
        # havaJoker : 是否含有大小王
        self.allcards = [] if havaJoker is False else ['joker', 'joker']
        for i in range(1, 14):
            for _ in range(4):
                self.allcards.append(i)

    def shuffle_card(self):
        # 洗牌
        random.shuffle(self.allcards)

    def take_card(self, n=1):
        # 抽牌
        your_card = []
        for _ in range(n):
            your_card.append(self.allcards.pop())
        return your_card

    def recovery(self, Ifshuffle=True):
        # 收牌，重新开始
        # Ifshuffle : 是否洗牌
        if Ifshuffle:
            self.__init__()
            self.shuffle_card()
        else:
            self.__init__()