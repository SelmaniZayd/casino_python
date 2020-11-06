import random
from modules.tirages import *
from modules.gain import calcul_gain
from modules.beautify import beautify_hand, beautify_card

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

# permet au joueur de choisir d'enlever ou de garder des cartes
def choix_carte(hand):
    new_hand = []
    for card in hand:
        beautify_card(card)
        print('Voulez vous garder la carte (y/n)? : ')
        user_answer = 'chalalala'
        while user_answer != 'y' and user_answer != 'n':
            user_answer = input()
        if user_answer == 'y':
            new_hand.append(card)
    return new_hand    



# retourne la main finale après le choix du joueur de garder/laisser des cartes
def machine():
    print('__________ PREMIER TIRAGE __________')
    hand, new_deck = premier_tirage(deck)
    beautify_hand(hand)

    print('________ LE CHOIX DES CARTES ________')
    hand = choix_carte(hand)

    print('__________ TIRAGE FINALE !__________')
    hand = deuxieme_tirage(hand, new_deck)
    beautify_hand(hand)

    return hand



def partie(mise, bankroll):
    bankroll -= mise
    text, gain = calcul_gain(machine(), mise)
    bankroll += gain
    print('---------------------------------------')
    print(text)
    print('---------------------------------------')
    print('VOTRE GAIN EST DE : ', gain, "$")
    return text, bankroll


def video_poker():
    bankroll = -1
    while bankroll <= 0:
        try:
            bankroll = int(input(" BANKROLL $$ : "))
        except:
            print("valeur incorrecte")
            bankroll = -1
        while bankroll > 0:
            mise = -1
            while mise > bankroll or mise <= 0:
                try:
                    mise = int(input(" Mise $: "))
                except:
                    print("valeur incorrecte")
            text, bankroll = partie(mise, bankroll)
            print('---------------------------------------')
            print("VOTRE BANKROLL : ", bankroll , ' $')
            print('---------------------------------------')
            
            replay = input('Rejouer ? y/n : ')
            if replay == 'n':
                exit()
video_poker()