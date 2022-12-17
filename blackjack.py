import random

def inrange(t: int, x: int, y: int):
    if t >= x and t <= y:
        return True
    else:
        return False

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