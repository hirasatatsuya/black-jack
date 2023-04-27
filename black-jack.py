import random
    
def main():
    # 1.プレイヤの持ち金を決める
    player_money = int(input("持ち金を入力してください。(例:1000)\n"))
    print(f"あなたの持ち金は{player_money}円です。\n")

    # 2.賭け金を決める
    player_bet = int(input("賭け金を入力してください。(例:200)\n"))
    print(f'賭け金は{player_bet}円です。\n')

    # 3.ゲームを行う
    SUITS = ['S', 'H', 'D', 'C'] # カードの柄
    CARDS_NUM = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # カードの数字
    CARD_VALUE = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} # 各カードの配点

    # 3-1.山札をシャッフル
    deck = []
    for suit in SUITS:
        for card_num in CARDS_NUM:
            deck.append
    player_hand = random.sample(CARD_NUM, 1)
    dealer_hand = random.sample(CARD_NUM, 1)
    print(f"\nプレイヤーの手札は{player_hand}です。")
    print(f"\nディーラーの手札は{dealer_hand}です。")


if __name__ == "__main__":
    main()
