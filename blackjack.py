import random
import sys

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
    index: int = None
    qualified: bool = True
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

playercount: int = None
if len(sys.argv) >= 2:
    try:
        playercount = int(sys.argv[1])
    except Exception as e:
        print("Invalid arguments. Additional info: ")
        print(e)
        exit()
else:
    playercount = 1

players = []
for i in range(playercount):
    players.append(Player(i + 1))

for player in players:
    loop: bool = True
    while loop:
        br: bool = False
        msg = "Player " + str(player.index) + ": "
        for c in player.cards:
            msg = msg + c.getDisplayName() + " "
        print(msg)
        choice = input("Hit [q], Stand [e]: ")
        switch choice:
            case "q":
                player.hit()
            case "e":
                loop = False
        if len(player.cards) == 2 and isBJ(player.getTotal()):
            print("BLACKJACK!")
            player.qualified = False
            loop = false
        if isBusted(player.getTotal()):
            print("BUST!")
            player.qualified = False
            loop = false
