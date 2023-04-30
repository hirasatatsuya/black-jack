import random

SUITS = ['S', 'H', 'D', 'C'] # カードの柄
CARDS_NUM = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # カードの数字
CARDS_VALUE = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} # 各カードの配点

# パーソンクラス
# プレイヤとディーラの手札、合計点を保持する
class Person(object):
    def __init__(self, money, bet):
        self.money = money # 持ち金
        self.bet = bet     # 賭け金
        self.hands = []    # 手札
        self.value = 0     # 合計点数

    def get_card(self, card):
        self.hands.append(card)
        self.value += CARDS_VALUE[card.card_value]
        if self.value > 21 and card.card_value == 'A':
            self.value -= 10

# カードクラス
class Card(object): # カードクラス
    def __init__(self, suit, card_value):
        self.suit = suit # カードの柄
        self.card_value = card_value # カードの数字と点数
    
    def __str__(self):
        return  self.suit + '-' + self.card_value 

def showInitialHand(player, dealer):
    print('\nディーラの手札:')
    print(f'1枚目:{dealer.hands[0]}\n2枚目: ?\n')
    print(f'\nプレイヤの手札:')
    for i, hand in enumerate(player.hands):
        print(f'{i+1}枚目:{hand}')
    print('\n')

def checkValue(person, person_name):
    if person.value > 21:
        print(f'{person_name}の手札:')
        for i, hand in enumerate(person.hands):
            print(f'{i+1}枚目:{hand}')
        print('バーストしました')
        return False
    else:
        print(f'{person_name}の手札:')
        for i, hand in enumerate(person.hands):
            print(f'{i+1}枚目:{hand}')
        return True

def exchangeBet(player, dealer, judgment):
    if judgment == 1:
        player.money += player.bet
        dealer.money -= dealer.bet
        print('\nプレイヤの勝利です。')
        print(f'プレイヤの持ち金は{player.money}です。')
        print(f'ディーラの持ち金は{dealer.money}です。')
    elif judgment == 2:
        player.money -= player.bet
        dealer.money += dealer.bet
        print('\nディーラの勝利です。')
        print(f'プレイヤの持ち金は{player.money}です。')
        print(f'ディーラの持ち金は{dealer.money}です。')
    elif judgment == 3:
        print('\n引き分けです。')

def main():
    # 1.プレイヤの持ち金を決める
    player_money = int(input("持ち金を入力してください。(例:1000)\n"))
    print(f"あなたの持ち金は{player_money}円です。")
    player = Person(player_money, 0) # プレイヤを初期化
    dealer = Person(player_money, 0) # ディーラを初期化

    while True:
        # 2.賭け金を決める
        player_bet = int(input("\n賭け金を入力してください。(例:200)\n"))
        print(f'賭け金は{player_bet}円です。\n')
        player = Person(player.money, player_bet) # プレイヤを初期化
        dealer = Person(dealer.money, player_bet) # ディーラを初期化

        # 3.ゲームを行う
        # 3-1.山札を作成
        deck = []
        for suit in SUITS:
            for card_value in CARDS_VALUE:
                deck.append(Card(suit, card_value))
        
        # 3-2.山札をシャッフル
        random.shuffle(deck)
        
        # 3-3.プレイヤ、ディーラに2枚づつ配り、合計点を計算
        for i in range (2):
            player.get_card(deck.pop())
            dealer.get_card(deck.pop())

        # 3-4.お互いのカードをオープン（ディーラは一枚を表にもう一枚は裏のまま）
        showInitialHand(player, dealer)

        # 3-5.プレイヤがヒットかスタンドを選択
        while True:
            selectedHitorStand = input('ヒットかスタンドを選択してください。ヒットの場合は「y」スタンドの場合は「n」を入力してください。\n')
            if selectedHitorStand == 'y':
                player.get_card(deck.pop())
                if checkValue(player, 'プレイヤ'):
                    continue
                else:
                    exchangeBet(player, dealer, 2) # プレイヤの負け
                    break
            elif selectedHitorStand == 'n':
                break
            else:
                print('error: yまたはn以外が入力されました。\n')
                continue
        print(f'プレイヤの合計点数 {player.value}\n')

        # 3-6.ディーラのターン
        if player.value <= 21:
            while dealer.value <= 16:
                dealer.get_card(deck.pop())
                if checkValue(dealer, 'ディーラ'):
                    continue
                else:
                    exchangeBet(player, dealer, 1) # ディーラの負け
                    break

            print(f'ディーラの手札:')
            for i, hand in enumerate(dealer.hands):
                print(f'{i+1}枚目:{hand}')
            print(f'ディーラの合計点数 {dealer.value}')
        
        # 3-7.プレイヤとディーラの合計点数を比較
        if player.value <= 21:
            if player.value > dealer.value: exchangeBet(player, dealer, 1) # プレイヤの勝利
            elif player.value < dealer.value: exchangeBet(player, dealer, 2) # ディーラの勝利
            elif player.value == dealer.value: exchangeBet(player, dealer, 3) # 引き分け

        # 4.プレイヤの持ち金を判断
        if player.money == 0:
            print('持ち金が0になりました。ゲームを終了します。')
            break
        elif player.money != 0:
            choiseContinue = input('ゲームを続けますか？')
            print(f'{choiseContinue}が入力されました')
            if choiseContinue == 'yes':
                continue
            elif choiseContinue == 'no':
                print('ゲームを終了します')
                break
        
if __name__ == "__main__":
    main()
