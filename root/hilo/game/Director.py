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




    def get_inputs(self):
        #asks the user if they choose a higher number or a lower number.


        #Args:
            #self(director):An instance of Director

        num_select=input("High or low? [h/l]")
        self.is_playing = input(num_select == "h")
        self.is_playing = input(num_select == "l")

    def do_updates(self):
        #draws a card
        #Args
            #self(Director) An instance of Director

        if not self.is_playing:
            return
        
        for i in range(len(self.card)):
            card = self.card
            card.draw()
            self.score += card.points
        self.total_score += self.score
    
    def do_outputs(self):
        #display results

        #Args:
            #self(Director): An instance of Director

            if not self.is_playing:
                return

            values = "" 
            for i in range(len(self.card)):


        

