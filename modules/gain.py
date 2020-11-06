from modules.combinaison import *

def calcul_gain(hand, mise):
    text = "Gagnant !! -- "

    if check_quinte_flush_royale(hand):
        text += "quinte flush royale !!!"
        mise *= 250
    elif check_quinte_flush(hand):
        text += "quinte flush !!!"
        mise *= 50
    elif check_carre(hand):
        text += "carre !!!"
        mise *= 25
    elif check_full(hand):
        text += " FUUUUUUUUUULLLL !!!"
        mise *= 9
    elif check_flush(hand):
        text += "flush !!!"
        mise *= 6
    elif check_quinte(hand):
        text += "quinte !!!"
        mise *= 4
    elif check_brelan(hand):
        text += " BRELANNN !!! "
        mise *= 3
    elif check_double_paire(hand):
        text += "double paire !!!"
        mise *= 2
    elif check_paire(hand):
        text += "paire !!!!"
        mise *= 1
    else:
        text = "bonne chance la prochaine fois"
        mise *= 0
    return text, mise