import random

class Dealer:

    def __init__(self):
        self.card = 0
        self.deal()
#starting cards is = to zero
    def deal(self):
        self.card = random.randint(1, 13)
        #random card is picked between 1 and 13
        

