from operator import truediv
from game.dealer import Dealer

class Director:
    # A person who directs the game.

    # The responsibility of the director is to control the game.
    
    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        

