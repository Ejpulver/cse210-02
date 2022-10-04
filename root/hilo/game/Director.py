from operator import truediv
from game.dealer import dealer

class Director:
    # A person who directs the game.

    # The responsibility of the director is to control the game.
    
    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.total_score = 300

    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        pass

    def do_updates(self):

        pass

    def do_outputs(self):
        
        pass




        

