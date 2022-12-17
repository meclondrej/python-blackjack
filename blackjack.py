import random

def inrange(t: int, x: int, y: int):
    if t >= x and t <= y:
        return True
    else:
        return False
def isBusted(x: int):
    if x > 21: return True
    else: return False
def isBJ(x: int):
    if x == 21: return True
    else: return False

class Card:
    value: int = None
    def __init__(self):
        self.value = random.randint(1, 13)
    def getDisplayName(self):
        if inrange(self.value, 2, 10):
            return str(self.value)
        else:
            switch self.value:
                case 1:
                    return "A"
                case 11:
                    return "J"
                case 12:
                    return "Q"
                case 13:
                    return "K"
class Player:
    cards = []
    def __init__(self):
        self.cards.append(Card())
        self.cards.append(Card())
    def hit(self):
        self.cards.append(Card())
    def getTotal(self):
        total: int = 0
        aces: int = 0
        for i in self.cards:
            if inrange(i.value, 2, 10):
                total = total + i.value
            else if inrange(i.value, 11, 13):
                total = total + 10
            else if i.value == 1:
                aces = aces + 1
        if aces > 0:
            for _ in range(aces):
                if (total + 11) > 21:
                    total = total + 1
                else:
                    total = total + 11