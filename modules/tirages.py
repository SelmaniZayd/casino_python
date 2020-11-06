import random

def premier_tirage(deck):
    hand = random.sample(deck, 5)
    return hand, [x for x in deck if x not in hand]

def deuxieme_tirage(hand, new_deck):
    return hand + random.sample(new_deck, 5 - len(hand))