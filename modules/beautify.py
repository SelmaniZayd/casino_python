from modules.Card import Card
from modules.Hand import Hand

def format_suits(hand):
    new_hand=hand.copy()
    for i in range(0,len(new_hand)):
        new_hand[i] = new_hand[i].replace('h', '1')
        new_hand[i] = new_hand[i].replace('d', '2')
        new_hand[i] = new_hand[i].replace('c', '3')
        new_hand[i] = new_hand[i].replace('s', '4')
    return new_hand

def beautify_hand(hand):
    h = Hand(format_suits(hand))
    h.print()

def beautify_card(card):
    card = card.replace('h', '1')
    card = card.replace('d', '2')
    card = card.replace('c', '3')
    card = card.replace('s', '4')
    b_card = Card(card.split('-')[0], int(card.split('-')[1]))
    b_card.print()