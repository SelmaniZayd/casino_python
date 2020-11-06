from modules.Card import Card

class Hand:
    def __init__(self,hand):
        self.hand = hand
    
    def print(self):
        cards = [Card(card.split('-')[0], int(card.split('-')[1])) for card in self.hand]
        lignes = ['','','','','','','']
        for card in cards:
            for i in range(0, len(card.lignes())):
                lignes[i] += card.lignes()[i]
        for ligne in lignes:
            print(ligne)