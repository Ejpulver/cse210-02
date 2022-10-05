import random

class Dealer:

    def __init__(self):

        self.points = 0
        self.value = 0

    
    def deal(self):

        self.value = random.randint(1, 13)
        

