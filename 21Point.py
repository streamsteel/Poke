from Poke import cards
import random

card = cards()
print('原始牌:', card.allcards)
card.shuffle_card()
print('洗牌后:', card.allcards)
print('21点双人比拼，第一轮游戏')
print('you\t\t\tme')
for i in range(10):
    you = card.take_card(random.choice([2,3,]))
    me = card.take_card(random.choice([2,3,]))
    print(you, '\t\t', me)
print('\n21点双人比拼，第二轮游戏')
card.recovery()
print('you\t\t\tme')
for i in range(10):
    you = card.take_card(random.choice([2,3,]))
    me = card.take_card(random.choice([2,3,]))
    print(you, '\t\t', me)