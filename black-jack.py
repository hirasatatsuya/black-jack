import random

SUITS = ['S', 'H', 'D', 'C'] # カードの柄
CARDS_VALUE = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} # 各カードの配点

# パーソンクラス
class Person(object): # プレイヤとディーラの手札、合計点を保持
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
class Card(object): # カードの初期化と柄と数字の組み合わせを作成
    def __init__(self, suit, card_value):
        self.suit = suit # カードの柄
        self.card_value = card_value # カードの数字と点数
    
    def __str__(self):
        return  self.suit + '-' + self.card_value 

def setBet(player, dealer): # 賭け金入力させる関数
    player_bet = int(input(f"「{min(player.money, dealer.money)}円」まで賭けれます。\n賭け金を入力してください。(例:200)\n"))
    if player_bet > min(player.money, dealer.money):
        print('持ち金以上の金額をかけています。持ち金以下の金額をベットしてください。\n')
        return setBet(player, dealer)
    print(f'賭け金は「{player_bet}円」です。\n')
    return player_bet

def showInitialHand(player, dealer): # プレイヤ・ディーラの初めの２枚の手札オープンさせる関数
    print('ーーーーーーーーーー\nディーラの手札:')
    print(f'1枚目:{dealer.hands[0]}\n2枚目: ?')
    print('--------------------\nプレイヤの手札:')
    for i, hand in enumerate(player.hands):
        print(f'{i+1}枚目:{hand}')
    print('ーーーーーーーーーー\n')

def checkValue(person, person_name): # 合計点数を計算し、バーストしたかを判断する関数
    print(f'\n「{person_name}」の手札:')
    for i, hand in enumerate(person.hands):
        print(f'{i+1}枚目:{hand}')
    print(f'{person_name} の合計点数 {person.value}\n')

    if person.value > 21: # バーストしたかどうかチェック
        print(f'「{person_name}」はバーストしました')
        return False
    else:
        return True

def exchangeBet(player, dealer, judgment): # ベット額の加減を計算する関数
    if judgment == 1:
        player.money += player.bet
        dealer.money -= dealer.bet
        print('\nプレイヤの勝利です。')
    elif judgment == 2:
        player.money -= player.bet
        dealer.money += dealer.bet
        print('\nディーラの勝利です。')
    elif judgment == 3:
        print('\n引き分けです。')
    print(f'「プレイヤ」の持ち金は{player.money}です。')
    print(f'「ディーラ」の持ち金は{dealer.money}です。')

def selectContinue(): # ゲームを続けるかを選択する関数
    choiseContinue = input('\nゲームを続けますか？ 続行する場合は"yes" 終了する場合は"no"\n')
    if choiseContinue == 'yes':
        print('\nゲームを続行します')
        return True
    elif choiseContinue == 'no':
        print('\nゲームを終了します')
        return False
    else:
        print('error: "yes"または"no"以外が入力されました。')
        return selectContinue()

def main():
    # 1.プレイヤの持ち金を決める
    player_money = int(input("持ち金を入力してください。(例:1000)\n"))
    print(f"あなたの持ち金は「{player_money}円」です。\n")
    player = Person(player_money, 0) # プレイヤの持ち金を初期化
    dealer = Person(player_money, 0) # ディーラの持ち金を初期化

    while True:
        # 2.賭け金を決める
        player_bet = setBet(player, dealer)
        player = Person(player.money, player_bet) # プレイヤを初期化
        dealer = Person(dealer.money, player_bet) # ディーラを初期化

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
            selectGetCard = input('ヒットかスタンドを選択してください。\nヒットの場合は「yes」スタンドの場合は「no」を入力してください。\n')
            if selectGetCard == 'yes': # ヒットの場合
                player.get_card(deck.pop())
                if checkValue(player, 'プレイヤ'): # 合計点計算ロジック
                    continue
                else:
                    exchangeBet(player, dealer, 2) # プレイヤの負け
                    break
            elif selectGetCard == 'no': # スタンドの場合
                checkValue(player, 'プレイヤ')
                break
            else:
                print('error: "yes"または"no"以外が入力されました。\n')
                continue

        # 3-6.ディーラのターン
        if player.value <= 21:
            checkValue(dealer, 'ディーラ')
            while dealer.value <= 16:
                dealer.get_card(deck.pop())
                if checkValue(dealer, 'ディーラ'):
                    continue
                else:
                    exchangeBet(player, dealer, 1) # ディーラの負け
                    break
        
        # 3-7.プレイヤとディーラの合計点数を比較
        if player.value <= 21 and dealer.value <= 21:
            if player.value > dealer.value: exchangeBet(player, dealer, 1) # プレイヤの勝利
            elif player.value < dealer.value: exchangeBet(player, dealer, 2) # ディーラの勝利
            elif player.value == dealer.value: exchangeBet(player, dealer, 3) # 引き分け

        # 4.プレイヤとディーラの持ち金を判断
        if player.money == 0:
            print('プレイヤの持ち金が0になりました。ゲームを終了します。')
            break
        elif dealer.money == 0:
            print('ディーラの持ち金が0になりました。プレイヤの完全勝利です。\nゲームを終了します。')
            break
        elif player.money != 0:
            choiseContinue = selectContinue() # ゲームを終了するか判定
            if choiseContinue == True: # ゲーム続行
                continue
            elif choiseContinue == False: # ゲーム終了
                break
        
if __name__ == "__main__":
    main()
