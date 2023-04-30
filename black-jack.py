import random

SUITS = ['S', 'H', 'D', 'C'] # カードの柄
CARDS_NUM = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # カードの数字
CARDS_VALUE = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} # 各カードの配点

# パーソンクラス
# プレイヤとディーラの手札、合計点を保持する
class Person(object):
    def __init__(self, money):
        self.money = money # 持ち金
        self.bet = 0       # 賭け金
        self.hand = []     # 手札
        self.value = 0     # 合計点数

    def get_card(self, card):
        self.hand.append(card)
        self.value += CARDS_VALUE[card.card_value]

# カードクラス
class Card(object): # カードクラス
    def __init__(self, suit, card_value):
        self.suit = suit # カードの柄
        self.card_value = card_value # カードの数字と点数
    
    def __str__(self):
        return  self.suit + '-' + self.card_value 

def main():
    # 1.プレイヤの持ち金を決める
    player_money = int(input("持ち金を入力してください。(例:1000)\n"))
    print(f"あなたの持ち金は{player_money}円です。\n")

    player = Person(player_money)
    dealer = Person(player_money)

    # 2.賭け金を決める
    player_bet = int(input("賭け金を入力してください。(例:200)\n"))
    print(f'賭け金は{player_bet}円です。\n')
    player.bet, dealer.bet = player_bet, player_bet

    # 3.ゲームを行う
    # 3-1.山札を作成
    deck = []
    for suit in SUITS:
        for card_value in CARDS_VALUE:
            deck.append(Card(suit, card_value))
    
    #3-2.山札をシャッフル
    random.shuffle(deck)
    
    #3-3.プレイヤ、ディーラに2枚づつ配り、
    for i in range (2):
        player.get_card(deck.pop())
        dealer.get_card(deck.pop())
        
if __name__ == "__main__":
    main()
