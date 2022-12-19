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
    def __init__(self):
        self.value = random.randint(1, 13)
    def getDisplayName(self):
        if inrange(self.value, 2, 10):
            return str(self.value)
        else:
            match self.value:
                case 1:
                    return "A"
                case 11:
                    return "J"
                case 12:
                    return "Q"
                case 13:
                    return "K"
class Player:
    def __init__(self, toindex: int):
        self.cards = []
        self.index: int = None
        self.qualified: bool = True
        self.cards.append(Card())
        self.cards.append(Card())
        self.index = toindex
    def hit(self):
        self.cards.append(Card())
    def getTotal(self):
        total: int = 0
        aces: int = 0
        for i in self.cards:
            if inrange(i.value, 2, 10):
                total = total + i.value
            elif inrange(i.value, 11, 13):
                total = total + 10
            elif i.value == 1:
                aces = aces + 1
        if aces > 0:
            for _ in range(aces):
                if (total + 11) > 21:
                    total = total + 1
                else:
                    total = total + 11
        return total
class Dealer(Player):
    def evaluateDealer(self):
        while not isBusted(self.getTotal()):
            if self.getTotal() > 17:
                self.hit()
            else:
                break

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

dealer = Dealer(0)
print("Dealer's first card: " + dealer.cards[0].getDisplayName())
players = []
for i in range(playercount):
    players.append(Player(i + 1))

for player in players:
    loop: bool = True
    while loop:
        msg = "Player " + str(player.index) + ": "
        for c in player.cards:
            msg = msg + c.getDisplayName() + " "
        print(msg)
        choice = input("Hit [q], Stand [e]: ")
        match choice:
            case "q":
                player.hit()
            case "e":
                loop = False
        if len(player.cards) == 2 and isBJ(player.getTotal()):
            msg = "Player " + str(player.index) + ": "
            for c in player.cards:
                msg = msg + c.getDisplayName() + " "
            print(msg)
            print("BLACKJACK!")
            player.qualified = False
            loop = False
        if isBusted(player.getTotal()):
            msg = "Player " + str(player.index) + ": "
            for c in player.cards:
                msg = msg + c.getDisplayName() + " "
            print(msg)
            print("BUST!")
            player.qualified = False
            loop = False

dealer.evaluateDealer()
dealermsg = "Dealer's hand: "
for c in dealer.cards:
    dealermsg = dealermsg + c.getDisplayName() + " "
print(dealermsg)
if isBusted(dealer.getTotal()):
    print("Dealer BUSTED!")
    for player in players:
        if not player.qualified: continue
        print("Player " + str(player.index) + " WON!")
elif len(dealer.cards) == 2 and isBJ(dealer.getTotal()):
    print("Dealer BLACKJACKED!")
    for player in players:
        if not player.qualified: continue
        print("Player " + str(player.index) + " LOST!")
else:
    for player in players:
        if not player.qualified: continue
        if player.getTotal() == dealer.getTotal():
            print("Player " + str(player.index) + " PUSHED!")
        if player.getTotal() > dealer.getTotal():
            print("Player " + str(player.index) + " WON!")
        if player.getTotal() < dealer.getTotal():
            print("Player " + str(player.index) + " LOST!")
