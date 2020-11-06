class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit-1] # 1,2,3,4 = ♥♦♣♠

    def lignes(self):
        return ['┌───────┐',f'| {self.value:<2}    |','|       |',f'|   {self.suit}   |','|       |',f'|    {self.value:>2} |','└───────┘']
    
    def print(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')