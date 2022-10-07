import random

class Dealer:

    def __init__(self):
        self.card = 0
        self.deal()

    def deal(self):
        self.card = random.randint(1, 13)
        

