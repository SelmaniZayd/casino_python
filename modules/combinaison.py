def check_carre(hand):
    hand_values = [card.split('-')[0] for card in hand]
    values_set = set(hand_values)
    if(len(values_set) == 2):
        counts = [hand_values.count(e) for e in values_set]
        if sorted(counts) == [1, 4]:
            return True
    return False

def check_paire(hand):
    hand_values = [card.split('-')[0] for card in hand]
    if len(set(hand_values)) == 4:
        return True

    return False

def check_brelan(hand):
    hand_values = [card.split('-')[0] for card in hand]
    values_set = set(hand_values)
    if len(values_set) == 3:
        counts = [hand_values.count(e) for e in values_set]
        if sorted(counts) == [1, 1, 3]:
            return True

    return False

def check_flush(hand):
    color = hand[0].split('-')[1]
        
    for i in range(1, len(hand)):
        if hand[i].split('-')[1] != color:
            return False
    return True

def __get_numbers_from_hand(hand):
    values = [card.split('-')[0] for card in hand]
    
    for n, i in enumerate(values):
        if i == 'J':
            values[n] = '11'
        if i == 'Q':
            values[n] = '12'
        if i == 'K':
            values[n] = '13'
        if i == 'A':
            values[n] = '14'
    
    numbers = [int(value) for value in values]
    numbers = sorted(numbers)
    return numbers

def check_quinte(hand):
    numbers = __get_numbers_from_hand(hand)

    if numbers == [2, 3, 4, 5, 14]:
        return True
    
    for i in range(0, len(numbers) - 1):
        if numbers[i+1] != numbers[i] + 1:
            return False
    return True
   
def check_quinte_flush(hand):
    if check_quinte(hand) and check_flush(hand):
        return True
    return False

def check_quinte_flush_royale(hand):
    matching_hand = ['10', 'J', 'Q', 'K', 'A']
    hand_values = [card.split('-')[0] for card in hand]

    does_match = True if sorted(matching_hand) == sorted(hand_values) else False

    if check_flush(hand) and does_match:
        return True
    return False

def check_full(hand):
    hand_values = [card.split('-')[0] for card in hand]
    values_set = set(hand_values)
    if(len(values_set) == 2):
        counts = [hand_values.count(e) for e in values_set]
        if sorted(counts) == [2, 3]:
            return True
    return False

def check_double_paire(hand):
    hand_values = [card.split('-')[0] for card in hand]
    values_set = set(hand_values)
    if(len(values_set) == 3):
        counts = [hand_values.count(e) for e in values_set]
        if sorted(counts) == [1, 2, 2]:
            return True
    return False