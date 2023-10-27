from itertools import product

numbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits=['S','H','D','C']

class card():
    def __init__(self, num, suit):
        self.number = num
        self.suit = suit

def classDeck():
    deck=[]
    for j in range(4):
        for k in range(13):
            deck.append(card(numbers[k],suits[j]))
    return deck

def tuplesDeck():
    quickDeck=product(numbers, suits)
    return quickDeck

def blackjackDeck():
    blackjackNums = numbers*4
    return (blackjackNums)
