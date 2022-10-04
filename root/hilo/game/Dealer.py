import random

class Dealer:

    def __init__(self):

        self.points = 0
        self.value = 0
        self.user_guess = 0

    
    def deal(self):

        self.value = random.randint(1, 13)
        if self.user_guess > self.value:
            self.points += 100
        elif self.user_guess < self.value:
            self.points -= 75
        else:
            self.points += 0
        

